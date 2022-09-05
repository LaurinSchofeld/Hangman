from os import stat
import random
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from .models import Word,Player,Game
from django.contrib.auth.models import User
import json


# Create your views here.




letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s = Word.objects.first()


def index(request):        
    return render(request,"hangman/index.html")

def newGame(request):
    if request.method == 'POST':
        lsPlayerGames = [] 
        name = request.POST['username']
        player = Player.objects.filter(userName = name)
        if player.exists():
          player = player.first()
          lsPlayerGames = Game.objects.filter(player=player)
        else:
          new_player = Player.objects.create(userName=name)
          new_player.save()
                  
        gCount = len(lsPlayerGames)
        
    random_word = random.choice(Word.objects.all())
    context = {
      'letters': letters, 
      #'word': random_word.word,
      'letter_placeholders': "_" * len(random_word.word),
      'gamesCount': gCount,
      'playerName': name, 
      'request': request
    }
    
    return render(request, "hangman/game.html", context)
    
    
def savegame(request):
    #hier where you save the game in th db
    #ask for new game
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     duration = request.POST["duration"]
    #     tries = request.POST["tries"]
    #     state = request.POST["state"]
    #     return render(request, "index.html", {
    #             "message": name
    #     })
    print(dir(request))
    post_data = json.loads(request.body.decode("utf-8"))
    player_name = post_data.get("player_name")
    game_duration = post_data.get("game_duration")
    tries_counter = post_data.get("tries_counter")
    is_solved = post_data.get("is_solved")
    player = Player.objects.filter(userName=player_name)
    if player.exists():
      player = player.first()
      Game.objects.create(player=player, duration=game_duration, tryes=tries_counter, result=is_solved)
      lsPlayerGames = Game.objects.filter(player=player)
      return HttpResponse(lsPlayerGames)
    else:
      return HttpResponseBadRequest(f"Kein Spieler unter dem Namen {player_name} gefunden")
    
      

    
