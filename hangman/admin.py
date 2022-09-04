from django.contrib import admin

from .models import Word,Player,Game

class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "player", "duration", "tryes", "date", "result")
    
class PlayerAdmin(admin.ModelAdmin):
    filter_horizontal = ("userName",)

admin.site.register(Word)
admin.site.register(Player)
admin.site.register(Game)

# Register your models here.
# test