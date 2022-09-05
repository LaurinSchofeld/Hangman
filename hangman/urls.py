from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="HangMan"),
    #path("<str:name>", views.checkName, name="NnewName"),
    #path("login",views.login_view, name="login"),
    path("newGame", views.newGame, name="newGame"),
    path("savegame/", views.savegame, name="savegame"),
    ]
