
from django.urls import path
# views
from games.views.game import (
    GamesListView ,
    GamesCreateView,
    GamesUpdateView,
    GamesDeleteView,
    GamesRetrieveView
)

app_name = 'games'

urlpatterns = [
    path('list/' , GamesListView.as_view() , name='games-list'),
    # create a new game
    path('create/' , GamesCreateView.as_view() , name='game-create'),
    # update a game
    path('update/<int:pk>/' , GamesUpdateView.as_view() , name='game-update'),
    # delete a game
    path('delete/<int:pk>/' , GamesDeleteView.as_view() , name='game-delete'),
    # retrieve a game
    path('retrieve/<int:pk>/' , GamesRetrieveView.as_view() , name='game-detail'),
]