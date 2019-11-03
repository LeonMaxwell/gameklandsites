from ckeditor.fields import RichTextField, RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.utils import timezone

from Library.models import InfoGames


class HeaderConstructorArticleGames(models.Model):
    name_article = models.ForeignKey(InfoGames, on_delete=models.CASCADE)
    name_header_article = models.CharField(max_length=250)
    about_header_article = models.TextField(default='')
    head_image = models.ImageField(upload_to='library_media', null=True, default='', editable=True, blank=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления статьи')
    slug = models.SlugField(max_length=250, unique_for_date='publish', default='', verbose_name='Слог шапки')

    class Meta:
        verbose_name = 'Добавить шапку статьи'
        verbose_name_plural = 'Добавить шапку для статей'

    def __str__(self):
        return self.name_header_article


class BodyConstructorArticleGame(models.Model):
    name_article = models.ForeignKey(InfoGames, on_delete=models.CASCADE)
    name_body_article = models.CharField(max_length=250)
    about_body_article = models.TextField(blank=True, default='')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления статьи')

    class Meta:
        verbose_name = 'Добавить заголовок статьи'
        verbose_name_plural = 'Добавить загловок для статей'

    def __str__(self):
        return '[' + self.name_article.article_name_info + ']' + self.name_body_article


class SubBodyConstructorArticleGame(models.Model):
    body_article = models.ForeignKey(BodyConstructorArticleGame, on_delete=models.CASCADE)
    sub_name_body_article = models.CharField(max_length=250)
    sub_body_image = models.ImageField(upload_to='library_media', null=True, default='', editable=True, blank=True)

    class Meta:
        verbose_name = 'Добавить под заголовок статьи'
        verbose_name_plural = 'Добавить под заголовок статей'

    def __str__(self):
        return '['+self.body_article.name_article.article_name_info+']' + '['+ self.body_article.name_body_article + \
               ']' + self.sub_name_body_article


class InfoCreateGalleryVideo(models.Model):
    COLOR_VIDEO_BLOCK = (
        ('white', 'Белый цвет'),
        ('red', 'Красный цвет')
    )
    name_article = models.ForeignKey(InfoGames, on_delete=models.CASCADE, default='')
    code_video = models.CharField(max_length=25)
    colors_video = models.CharField(max_length=25, choices=COLOR_VIDEO_BLOCK)

    class Meta:
        verbose_name = 'Редактор видео-плеера'
        verbose_name_plural = 'Редактор видео-плееров'

    def __str__(self):
        return 'Видео-плеер' + str(self.pk)


class ImageGallery(models.Model):
    name_article = models.ForeignKey(InfoGames, on_delete=models.CASCADE)
    image_input = models.ImageField(upload_to='library_media', null=True, default='', editable=True, blank=True)

    class Meta:
        verbose_name = 'Добавление картинки в галлерею'
        verbose_name_plural = 'Добавление картинок в галлерею'

    def __str__(self):
        return 'Картинка ' + str(self.pk)


class ContentSubBodyConstructorArticleGame(models.Model):
    sub_name_article = models.ForeignKey(SubBodyConstructorArticleGame, default='', on_delete=models.CASCADE)
    text_content = RichTextField(default='', null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления статьи')

    class Meta:
        verbose_name = 'Добавить контент в заголовок статьи'
        verbose_name_plural = 'Добавить контент в заголовок статей'

    def __str__(self):
        return 'Контент ' + str(self.pk)
