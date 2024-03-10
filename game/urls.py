
from django.contrib import admin
from django.urls import path, include
from .views import GameView

urlpatterns = [
    path('', GameView.as_view(), name='game'),   
]
