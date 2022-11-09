
from django.core.management import BaseCommand
from games.providers.games_loader import load_games_to_db

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_games_to_db()

    
# to run the command : python manage.py load_games
 