from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from games.models import Game , Platform
from games.providers.games_loader import load_games_to_db

# disable warnings cause i kinda hate them
import warnings
warnings.filterwarnings("ignore")


# endpoints
GAMES_LIST_URL = reverse('games:games-list')

class GameFilterTestAPI(TestCase):

    def setUp(self) :
        # add client that will be used to make requests
        self.client = APIClient()
        # load games to db
        load_games_to_db()

    def test_set_up(self):
        # make sure that games were loaded to db are not empty
        self.assertTrue(Game.objects.all().count() > 0)
        # print a green message saying that the test passed
        print('\033[92m' + 'test_set_up passed' + '\033[0m')

    def test_filter_by_platform(self):
        print("**********Starting test_filter on games list api view**********")
        games_count = Game.objects.all().count()
        # make a get request to the games endpoint
        res = self.client.get(GAMES_LIST_URL )
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        
        games_loaded = res.data['results']
        # make sure that the response is not empty
        self.assertTrue(len(games_loaded) > 0)

        # set filter to be used in the request params
        params = {
            "game" : "World of warcraft",
            "user_id" : 7,
        }
        # re call the api with the filter params 
        res = self.client.get(GAMES_LIST_URL , params)
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the games returned from the api
        games_loaded = res.data['results']
        # make sure that the response is >= 1 game
        self.assertTrue(len(games_loaded) >= 1)
        print('\033[92m' + 'test_filter_by_platform passed with game name and user_id' + '\033[0m')

        params = {
            "platforms" : "PC,PS4",
        }
        # re call the api with the filter params
        res = self.client.get(GAMES_LIST_URL , params)
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the games returned from the api
        games_loaded = res.data['results']
        # make sure that the response is not empty
        self.assertTrue(len(games_loaded) > 0)
        # make sure that len games loaded is less than games count
        self.assertTrue(len(games_loaded) < games_count)

        print('\033[92m' + 'test_filter_by_platform passed with platforms' + '\033[0m')

        params = {
            "order_by" : "play_time",
            "page_size" : 1000,
        }
        # re call the api with the filter params
        res = self.client.get(GAMES_LIST_URL , params)
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the games returned from the api
        loaded_games_play_time = res.data['results']

        params = {
            "order_by" : "-play_time",
            "page_size" : 1000,
        }
        # re call the api with the filter params
        res = self.client.get(GAMES_LIST_URL , params)
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the games returned from the api
        loaded_games_play_time_desc = res.data['results']

        # make sure that loaded_games_play_time and loaded_games_play_time_desc are the reverse of each other
        names = [game['game'] for game in loaded_games_play_time_desc]
        names_2=[game['game'] for game in loaded_games_play_time]
        self.assertTrue(names == names_2[::-1])
        # print a green message saying that the test passed
        print('\033[92m' + 'test_filter_by_platform passed with order by' + '\033[0m')

        # test on wrong game name
        params = {
            "game" : "wit",
        }
        # re call the api with the filter params
        res = self.client.get(GAMES_LIST_URL , params)
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the games returned from the api
        games_loaded = res.data['results']
        # make sure that the response is not empty
        self.assertTrue(len(games_loaded) > 0)
        # print a green message saying that the test passed
        print('\033[92m' + 'test_filter_by_platform passed with wrong game name' + '\033[0m')

        

# to run this test use the following command : python manage.py test games.tests.test_games_filter.GameFilterTestAPI