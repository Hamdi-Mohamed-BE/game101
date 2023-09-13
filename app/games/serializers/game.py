from rest_framework import serializers

# models
from games.models import Game , Platform


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('name',)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GameCreateSerializer(serializers.ModelSerializer):
    
    platforms = PlatformSerializer(many=True , read_only=True)

    platforms_names = serializers.ListField(
        child=serializers.CharField(max_length=100),
        write_only=True,
        required=False
    )

    def create(self , validated_data):
        # same here we can add logic to be used with the requesting user
        
        # pop the platforms_names from the validated_data
        platforms_names = validated_data.pop('platforms_names' , None)
        # create the game
        game = super().create(validated_data)
        # assign the platforms to the game using get or create
        if platforms_names:
            for platform_name in platforms_names:
                platform , _  = Platform.objects.get_or_create(
                    name=platform_name
                )
                game.platforms.add(platform)
        return game
    
    class Meta:
        model = Game
        fields = (
            'id' ,
            'user_id' ,
            'game' ,
            'play_time' ,
            'genre' ,
            'platforms_names',
            'platforms',
        )


class GameUpdateSerializer(serializers.ModelSerializer):
    platforms = PlatformSerializer(many=True , read_only=True)

    platforms_names = serializers.ListField(
        child=serializers.CharField(max_length=100),
        write_only=True
    )

    def update(self , instance , validated_data):
        # same here we can add logic to be used with the requesting user
        
        # pop the platforms_names from the validated_data
        platforms_names = validated_data.pop('platforms_names' , None)
        # update the game
        game = super().update(instance , validated_data)
        # assign the platforms to the game using get or create
        if platforms_names:
            for platform_name in platforms_names:
                platform , _  = Platform.objects.get_or_create(
                    name=platform_name
                )
                game.platforms.add(platform)
        return game
    
    class Meta:
        model = Game
        fields = (
            'game' ,
            'play_time' ,
            'genre' ,
            'platforms_names',
            'platforms',
        )

