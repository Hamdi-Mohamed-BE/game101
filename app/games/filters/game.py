from rest_framework.serializers import ValidationError
from games.models import Game
from django_filters import rest_framework as filters


class GameFilter(filters.FilterSet):
    # user_id use exaclty lookup
    user_id = filters.NumberFilter(field_name='user_id' , lookup_expr='exact')
    # platforms use filter method
    platforms = filters.CharFilter(method='filter_platforms')
    # game use filter method use icontains lookup
    game = filters.CharFilter(field_name='game' , lookup_expr='icontains')
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
