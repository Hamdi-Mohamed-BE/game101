# rest framework
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , UpdateAPIView , DestroyAPIView
from rest_framework.serializers import ValidationError
# swagger
from drf_yasg.utils import swagger_auto_schema 
from rest_framework.decorators import parser_classes
from drf_yasg import openapi
# models
from games.models import Game
# filters
from games.filters.game import GameFilter
from django_filters import rest_framework as filters

# serializers
from games.serializers.game import GameSerializer

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