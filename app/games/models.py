from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=100 , unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    user_id = models.IntegerField()
    
    game = models.CharField(max_length=100)

    play_time = models.IntegerField()
    genre = models.CharField(max_length=100)
    platforms = models.ManyToManyField(
        Platform , 
        related_name='games' , 
        blank=True
    )

    def __str__(self):
        return self.game
