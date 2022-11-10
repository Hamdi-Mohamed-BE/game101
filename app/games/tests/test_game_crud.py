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


class GameCRUDTestAPI(TestCase):

    def setUp(self) :
        # add client that will be used to make requests
        self.client = APIClient()
    
    def test_game_create_api(self):
        # set the payload to be used in the post request
        payload = {
            "user_id" : 7, # this should be required
            "game" : "World of warcraft TEST", # this should be required
            "play_time" : 100, # this should be required
            "genre" : "MMORPG", # this should be required
            "platforms" : [
                "PC",
                "PS4",
            ]
        }
        # ***** NOTE:
        # * please note for platforms now we are just trying get or create the platform if it's not there
        # * this can be changed when we set a defined list of platforms on the db from the beginning

        # load list of games from the api list endpoint
        res = self.client.get(GAMES_LIST_URL)
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the games returned from the api
        games_loaded = res.data['results']
        # games now are empty   
        self.assertTrue(len(games_loaded) == 0)

        # make a post request to the games:game-create endpoint
        res = self.client.post(reverse('games:game-create') , payload , format='json')
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_201_CREATED)
        # load list of games from the api list endpoint
        res = self.client.get(GAMES_LIST_URL)
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the games returned from the api
        games_loaded = res.data['results']
        # games now are not empty
        self.assertTrue(len(games_loaded) > 0)
        # print a green message saying that the test passed
        print('\033[92m' + 'test_game_create_api passed' + '\033[0m')

    def test_game_create_api_with_invalid_payload(self):
        payload = {
            "game" : "World of warcraft TEST", # this should be required
            "play_time" : 100, # this should be required
            "genre" : "MMORPG", # this should be required
            "platforms" : [
                "PC",
                "PS4",
            ]
        }
        # make a post request to the games:game-create endpoint
        res = self.client.post(reverse('games:game-create') , payload , format='json')
        # make sure that the request was not successful
        self.assertEqual(res.status_code , status.HTTP_400_BAD_REQUEST)
    
    def test_game_retrieve_api(self):
        # call the games:game-detail endpoint with the pk as the game id (in this case is not created yet)
        res = self.client.get(reverse('games:game-detail' , kwargs={'pk' : 2531}))
        # make sure that the request was not successful
        self.assertEqual(res.status_code , status.HTTP_404_NOT_FOUND)
        
        # set the payload to be used in the post request
        payload = {
            "user_id" : 7, # this should be required
            "game" : "World of warcraft TEST", # this should be required
            "play_time" : 100, # this should be required
            "genre" : "MMORPG", # this should be required
            "platforms_names" : [
                "PC",
                "PS4",
            ]
        }
        # make a post request to the games:game-create endpoint
        res = self.client.post(reverse('games:game-create') , payload , format='json')
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_201_CREATED)
        # get the game id from the response
        game_id = res.data['id']

        # call the games:game-detail endpoint with the pk as the game id
        res = self.client.get(reverse('games:game-detail' , kwargs={'pk' : game_id}))
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the game returned from the api
        game_loaded = res.data
        # make sure that the game returned is the same as the one we created
        self.assertEqual(game_loaded['game'] , payload['game'])
        self.assertEqual(game_loaded['play_time'] , payload['play_time'])
        self.assertEqual(game_loaded['genre'] , payload['genre'])
        # print a green message saying that the test passed
        print('\033[92m' + 'test_game_retrieve_api passed' + '\033[0m')

    def test_update_game(self):
        # set the payload to be used in the post request
        payload = {
            "user_id" : 7, # this should be required
            "game" : "World of warcraft TEST", # this should be required
            "play_time" : 100, # this should be required
            "genre" : "MMORPG", # this should be required
            "platforms_names" : [
                "PC",
                "PS4",
            ]
        }
        # make a post request to the games:game-create endpoint
        res = self.client.post(reverse('games:game-create') , payload , format='json')
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_201_CREATED)
        # get the games returned from the api
        game_loaded = res.data
        # get the game id from the response
        game_id = game_loaded['id']

        # call the games:game-detail endpoint with the pk as the game id
        res = self.client.get(reverse('games:game-detail' , kwargs={'pk' : game_id}))
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the game returned from the api
        game_loaded = res.data
        # make sure that the game returned is the same as the one we created
        self.assertEqual(game_loaded['game'] , payload['game'])
        self.assertEqual(game_loaded['play_time'] , payload['play_time'])
        self.assertEqual(game_loaded['genre'] , payload['genre'])

        # set the payload to be used in the put request
        payload = {
            "game" : "World of warcraft TEST UPDATED", # this should be required
            "play_time" : 500, # this should be required
            "genre" : "MMORPG", # this should be required
            "platforms_names" : [
                "PC",
                "PS4",
                "XBOX"
            ]
        }
        # make a put request to the games:game-update endpoint
        res = self.client.put(reverse('games:game-update' , kwargs={'pk' : game_id}) , payload , format='json')
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the game returned from the api
        game_loaded = res.data
        # make sure that the game returned is the same as the one we created
        self.assertEqual(game_loaded['game'] , payload['game'])
        self.assertEqual(game_loaded['play_time'] , payload['play_time'])
        self.assertEqual(game_loaded['genre'] , payload['genre'])
        self.assertEqual(len(game_loaded['platforms']) , len(payload['platforms_names']))
        # print a green message saying that the test passed
        print('\033[92m' + 'test_update_game passed' + '\033[0m')

    def test_delete_game(self):
         # set the payload to be used in the post request
        payload = {
            "user_id" : 7, # this should be required
            "game" : "World of warcraft TEST", # this should be required
            "play_time" : 100, # this should be required
            "genre" : "MMORPG", # this should be required
            "platforms" : [
                "PC",
                "PS4",
            ]
        }
        # make a post request to the games:game-create endpoint
        res = self.client.post(reverse('games:game-create') , payload , format='json')
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_201_CREATED)
        # get the games returned from the api
        game_loaded = res.data
        # get the game id from the response
        game_id = game_loaded['id']

        # call games:game-delete endpoint with the pk as the game id
        res = self.client.delete(reverse('games:game-delete' , kwargs={'pk' : game_id}))
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_204_NO_CONTENT)
        # re load the games from the api
        res = self.client.get(reverse('games:games-list'))
        # make sure that the request was successful
        self.assertEqual(res.status_code , status.HTTP_200_OK)
        # get the games returned from the api
        games_loaded = res.data['results']
        # games now are empty
        self.assertTrue(len(games_loaded) == 0)
        # print a green message saying that the test passed
        print('\033[92m' + 'test_delete_game passed' + '\033[0m')


# to run the tests run the following command : python manage.py test games.tests.test_game_crud.GameCRUDTestAPI