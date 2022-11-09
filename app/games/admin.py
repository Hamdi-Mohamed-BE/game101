from django.contrib import admin

# Register your models here.
from games.models import Game , Platform

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
