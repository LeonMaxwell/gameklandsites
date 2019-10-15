from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.library, name='Library'),
    path('games/', views.content, name='LibraryGames'),
    path('games/<str:name_game>', views.content_games, name='LibraryGamesArticle'),
    path('aboutKlan/', views.aboutKlan, name='LibraryAboutKlan'),
]