
from django.urls import path
# views
from games.views.game import (
    GamesListView ,
)

app_name = 'games'

urlpatterns = [
    path('' , GamesListView.as_view() , name='games-list'),
]