from django.urls import path

from . import views

urlpatterns = [
    path('', views.library, name='Library'),
    path('games/', views.content, name='LibraryGames'),
    path('aboutKlan/', views.aboutKlan, name='LibraryAboutKlan'),
]