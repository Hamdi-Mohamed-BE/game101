from rest_framework.serializers import ValidationError
from games.models import Game
from django_filters import rest_framework as filters
from django.db.models import Q
# auto correct for the game names
from autocorrect import Speller

# defautl spelling corrector is in english
spell = Speller(lang='en')

# a function to ge the closest match for a word in list of words
def get_close_matches(word  , list_of_word):
    """
        -The main idea is to loop through the list of words and get the closest match
        -The closest match we need to get how many letters are the same
    """
    score = 0
    closest = list_of_word[0]
    for w in list_of_word[1:]:
        # get the number of letters that are the same
        same_letters = sum(1 for a, b in zip(word, w) if a == b)
        # if the number of same letters is greater than the current score
        # then update the score
        if same_letters > score:
            score = same_letters
            closest = w
    return closest


class GameFilter(filters.FilterSet):
    # user_id use exaclty lookup
    user_id = filters.NumberFilter(field_name='user_id' , lookup_expr='exact')
    # platforms use filter method
    platforms = filters.CharFilter(method='filter_platforms')
    # game use filter method 
    game = filters.CharFilter(method='filter_game')
    # genre use filter method use icontains lookup
    genre = filters.CharFilter(field_name='genres__name' , lookup_expr='icontains')

    # order_by use filter method
    order_by = filters.CharFilter(method='filter_order_by') 


    class Meta:
        model = Game
        fields = (
            'user_id' ,
            'platforms' ,
            'game' ,
            'genre' ,
            'order_by'
        )
    
    def filter_game(self , queryset , name , value):
        if value:
            spelled_value = spell(value)
            # get the games names from data base as discinct values
            games_names = queryset.values_list('game' , flat=True).distinct()
            if spelled_value not in games_names:
                # here we get the closest match to the game name
                closet_match = get_close_matches(spelled_value , games_names)
            # update the qureyset
            queryset = queryset.filter(
                Q(game__icontains=spelled_value) | 
                Q(game__icontains=value) |
                Q(game__icontains=closet_match)
            )
        return queryset

    def filter_platforms(self , queryset , name , value):
        if value:
            platforms = value.split(',')
            queryset = queryset.filter(platforms__name__in=platforms)
        return queryset
    
    def filter_order_by(self , queryset , name , value):
        allowed_order_by = ['play_time' , '-play_time']
        if value:
            if value not in allowed_order_by:
                raise ValidationError(f"order_by must be one of {allowed_order_by}")
            queryset = queryset.order_by(value)
        return queryset
