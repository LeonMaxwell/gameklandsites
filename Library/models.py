from django.db import models


# Create your models here.

class AboutLibrary(models.Model):
    id_room = 4
    name_room = models.CharField(max_length=20)
    about_room = models.TextField(max_length=56)
    image_room = models.ImageField(upload_to='library_media')

    def __str__(self):
        return self.name_room


class SectionInLibraryAboutGames(models.Model):
    name_section = models.CharField(max_length=20)
    about_section = models.TextField(max_length=56)
    image_section = models.ImageField(upload_to='library_media')

    def __str__(self):
        return self.name_section


class ContentsInSectionGames(models.Model):
    name_game = models.CharField(max_length=20)
    brief_information_for_games = models.TextField(max_length=56)
    image_games = models.ImageField(upload_to='library_media')

    def __str__(self):
        return self.name_game

class InfoGames(models.Model):
    name_games = models.ForeignKey(ContentsInSectionGames, on_delete=models.CASCADE, default='',editable=True)
    heading_name_info = models.CharField(max_length=20)
    pictures_for_info = models.ImageField(upload_to='library_media', default='',editable=True)

    def __str__(self):
        return self.heading_name_info

class BaseInfoGame(models.Model):

    name_game = models.ForeignKey(ContentsInSectionGames, on_delete=models.CASCADE, default='',editable=True)
    section_name_info = models.ForeignKey(InfoGames, on_delete=models.CASCADE, default='', editable=True)
    head_name = models.CharField(max_length=50, default='', editable=True)
    info_section_on_games = models.TextField(max_length=500, default='', editable=True)
    picture_section_on_games = models.ImageField(upload_to='library_media', default='', editable=True)
    url_video = models.CharField(max_length=50, default='', editable=True)

    def __str__(self):
        return self.head_name

class SectionInLibraryAboutKlan(models.Model):
    name_section = models.CharField(max_length=20)
    about_section = models.TextField(max_length=56)
    image_section = models.ImageField(upload_to='library_media')

    def __str__(self):
        return self.name_section



