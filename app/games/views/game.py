# rest framework
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView , CreateAPIView ,
    RetrieveAPIView , UpdateAPIView , 
    DestroyAPIView
)
# swagger
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
# models
from games.models import Game
# filters
from games.filters.game import GameFilter
from django_filters import rest_framework as filters
# serializers
from games.serializers.game import (
    GameSerializer , 
    GameCreateSerializer ,
    GameUpdateSerializer
)


# views to write
class GamesListView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_class = GameFilter
    
    # override the get method to add the filter to swagger
    @swagger_auto_schema(
        manual_parameters=[
            # user_id
            openapi.Parameter(
                name='user_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='user id',
                required=False
            ),
            # platforms
            openapi.Parameter(
                name='platforms' ,
                in_=openapi.IN_QUERY ,
                description='Filter by platforms' ,
                type=openapi.TYPE_STRING
            ),
            # game
            openapi.Parameter(
                name='game' ,
                in_=openapi.IN_QUERY ,
                description='Filter by game name' ,
                type=openapi.TYPE_STRING
            ),
            # genre
            openapi.Parameter(
                name='genre' ,
                in_=openapi.IN_QUERY ,
                description='Filter by genre' ,
                type=openapi.TYPE_STRING
            ),
            #order_by
            openapi.Parameter(
                name='order_by' ,
                in_=openapi.IN_QUERY ,
                description='Order by choices are (play_time , -play_time)' ,
                type=openapi.TYPE_STRING
            ),
        ]
    )
    def get(self , request , *args , **kwargs):
        return super().get(request , *args , **kwargs)


class GamesCreateView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer


class GamesRetrieveView(RetrieveAPIView):
    serializer_class = GameSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Game , pk=pk)


class GamesUpdateView(UpdateAPIView):
    serializer_class = GameUpdateSerializer
    # allow on PUT method
    allowed_methods = ['PUT']


    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Game , pk=pk)


class GamesDeleteView(DestroyAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    def get_object(self):
        # here we can add logic to check if the user is the owner of the game (the requesting user)
        # or just add permissions class to the view + with authentication permission classes
        pk = self.kwargs.get('pk')
        return get_object_or_404(Game , pk=pk)