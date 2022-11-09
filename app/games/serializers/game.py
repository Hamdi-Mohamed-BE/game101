from rest_framework import serializers

# models
from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'