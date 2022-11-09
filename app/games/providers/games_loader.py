"""
    This file we will set a simple function to load the games from the json file to our database
"""
import json
import os
from games.models import Game , Platform

# current directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_games_to_db()-> None:
    """
        This function will load the games from the json file to our database
    """
    # open the json file
    with open(os.path.join(CURRENT_DIR, 'games.json'), 'r') as file:
        # load the json file
        games = json.load(file).get('data')
        # loop over the games
        for game in games:
            selected_platforms = []
            platforms = game.pop('platforms')
            # loop over the platforms 
            for platform in platforms:
                # get the platform object
                platform_obj , _  = Platform.objects.get_or_create(
                    name=platform
                )
                # append the platform object to the selected platforms list
                selected_platforms.append(platform_obj)

            instance , _ = Game.objects.get_or_create(
                game=game['game'],
                user_id=game['userId'],
                defaults={
                    'play_time': game['playTime'],
                    'genre': game['genre'],
                }
            )
            # add the platforms to the game
            instance.platforms.add(*selected_platforms)
            # save the game
            instance.save()
            # print green message saying that the game is saved successfully
            print(f'\033[92m{game["game"]} is saved successfully\033[0m')