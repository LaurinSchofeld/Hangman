from datetime import datetime
from time import time
from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=16)
    
    def __str__(self):
        return f"{self.id, self.word}"
    
class Player(models.Model):
    userName = models.CharField(max_length=8,unique=True)
    
    def __str__(self):
        return f"{self.id, self.userName}"
    
class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    duration = models.IntegerField()
    tryes = models.IntegerField()
    date = models.DateField(default=datetime.now())
    result = models.BooleanField()
    
    def __str__(self):
        return f"{self.id, self.player, self.duration, self.tryes, self.date, self.result}"