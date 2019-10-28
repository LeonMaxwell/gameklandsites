from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(HeaderConstructorArticleGames)
class HeaderConstructorArticleGamesAdmin(admin.ModelAdmin):
    list_display = ('name_header_article', 'name_article', 'slug', 'pk',  'publish', 'update')
    list_filter = ('name_article', 'publish', 'update')
    search_fields = ('name_article', 'name_header_article')
    prepopulated_fields = {'slug': ('name_header_article', )}
    date_hierarchy = 'publish'
    ordering = ('name_article', 'name_header_article', 'publish')


@admin.register(BodyConstructorArticleGame)
class BodyConstructorArticleGameAdmin(admin.ModelAdmin):
    list_display = ('name_article', 'name_body_article', 'pk',  'publish', 'update')
    list_filter = ('name_article', 'publish', 'update')
    search_fields = ('name_article', 'name_body_article')
    date_hierarchy = 'publish'
    ordering = ('name_article', 'name_body_article', 'publish')


@admin.register(SubBodyConstructorArticleGame)
class SubBodyConstructorArticleGameAdmin(admin.ModelAdmin):
    list_display = ('sub_name_body_article', 'body_article', '__str__',)
    list_filter = ('sub_name_body_article', 'body_article')
    search_fields = ('sub_name_body_article', 'body_article')
    ordering = ('body_article',)


admin.site.register(InfoCreateGalleryVideo)
admin.site.register(ImageGallery)
@admin.register(ContentSubBodyConstructorArticleGame)
class ContentSubBodyConstructorArticleGameAdmin(admin.ModelAdmin):
    list_display = ('sub_name_article', 'pk', 'publish',  'update', '__str__')
    date_hierarchy = 'publish'
