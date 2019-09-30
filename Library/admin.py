from django.contrib import admin
from .models import AboutLibrary, SectionInLibraryAboutGames, SectionInLibraryAboutKlan, ContentsInSectionGames,InfoGames,BaseInfoGame

admin.site.register(AboutLibrary)
admin.site.register(SectionInLibraryAboutGames)
admin.site.register(InfoGames)
admin.site.register(BaseInfoGame)
admin.site.register(ContentsInSectionGames)
admin.site.register(SectionInLibraryAboutKlan)