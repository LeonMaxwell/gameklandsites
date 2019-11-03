from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.utils import timezone


class AboutLibrary(models.Model):
    id_room = 4
    name_room = models.CharField(max_length=20)
    about_room = models.TextField(max_length=56)
    image_room = models.ImageField(upload_to='library_media')

    class Meta:
        verbose_name = 'О библиотеке'
        verbose_name_plural = 'О библиотеке'

    def __str__(self):
        return self.name_room


class SectionInLibraryAboutKlan(models.Model):
    name_section = models.CharField(max_length=20)
    about_section = models.TextField(max_length=56)
    image_section = models.ImageField(upload_to='library_media')

    class Meta:
        verbose_name = 'Секция клана в Библиотеке'
        verbose_name_plural = 'Секция клана в Библиотеке'

    def __str__(self):
        return self.name_section


class SectionInLibraryAboutGames(models.Model):
    name_section = models.CharField(max_length=20)
    about_section = models.TextField(max_length=56)
    image_section = models.ImageField(upload_to='library_media')

    class Meta:
        verbose_name = 'Секция игр в Библиотеке'
        verbose_name_plural = 'Секция игр в Библиотеке'

    def __str__(self):
        return self.name_section


class ContentsInSectionGames(models.Model):
    name_game = models.CharField(max_length=20)
    image_games = models.ImageField(upload_to='library_media')

    class Meta:
        verbose_name = 'О игре'
        verbose_name_plural = 'О играх'
        ordering = ('name_game',)

    def __str__(self):
        return self.name_game


class InfoGames(models.Model):
    name_games = models.ForeignKey(ContentsInSectionGames, on_delete=models.CASCADE, default='', editable=True,
                                   verbose_name='Название игры')
    article_name_info = models.CharField(max_length=20, verbose_name='Название статьи игры')
    pictures_for_info = models.ImageField(upload_to='library_media', default='', editable=True,
                                          verbose_name='Картинка статьи')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    slug = models.SlugField(max_length=250, unique_for_date='publish', default='', verbose_name='Слог статьи')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления статьи')

    class Meta:
        verbose_name = 'Статья о игре'
        verbose_name_plural = 'Статьи о игре'
        ordering = ('-article_name_info',)

    def __str__(self):
        return self.article_name_info


class ContentAboutKlan(models.Model):
    name_content_about_klan = RichTextField(verbose_name='Имя заголовка')
    text_content_about_klan = RichTextField(blank=True, null=True, verbose_name='Текст заголовка')

    class Meta:
        verbose_name = 'Информация о клане'
        verbose_name_plural = 'Информации о клане'

    def __str__(self):
        return self.name_content_about_klan
