from django.contrib import admin
from .models import *

admin.site.register(AboutLibrary)
admin.site.register(SectionInLibraryAboutGames)

@admin.register(InfoGames)
class InfoGamesAdmin(admin.ModelAdmin):
    list_display = ('article_name_info', 'name_games',  'slug', 'publish', 'update')
    list_filter = ('name_games', 'publish', 'update')
    search_fields = ('name_games', 'article_name_info')
    prepopulated_fields = {'slug': ('article_name_info',)}
    date_hierarchy = 'publish'
    ordering = ('article_name_info', 'name_games', 'publish')

admin.site.register(ContentsInSectionGames)
admin.site.register(SectionInLibraryAboutKlan)