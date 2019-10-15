from django.shortcuts import render

from BattlleField.models import AboutBattleField
from Dungeon.models import AboutDungeon
from MainHall.models import AboutMainHall
from PoolOfMemory.models import AboutPoolOfMemory
from RoundTable.models import AboutRoundTable
from .models import AboutLibrary, SectionInLibraryAboutGames, SectionInLibraryAboutKlan, ContentsInSectionGames, \
    InfoGames


def library(request):
    my_data = AboutLibrary.objects.all()
    dat_game = SectionInLibraryAboutGames.objects.all()
    dat_klan = SectionInLibraryAboutKlan.objects.all()
    content_battlefield = AboutBattleField.objects.all()
    content_dungeon = AboutDungeon.objects.all()
    content_pool_of_memory = AboutPoolOfMemory.objects.all()
    content_round_table = AboutRoundTable.objects.all()
    content_main_hall = AboutMainHall.objects.all()
    contaxt = {"prTitle": "Библиотека",
               "data": my_data,
               "selectGame": dat_game,
               "selectKlan": dat_klan,
               "battlefield": content_battlefield,
               "dungeon": content_dungeon,
               "pool_of_memory": content_pool_of_memory,
               "round_table": content_round_table,
               "main_hall": content_main_hall,
               "this_path": request.get_full_path()}
    return render(request, "connects/library_parts.html", contaxt)


def content(request):
    data_selection = ContentsInSectionGames.objects.all()
    inf_g = InfoGames.objects.all()
    count = {inf_g[i].name_games: 'Кол-во статей: '+str(inf_g.filter(name_games=inf_g[i].name_games).count()) for i in range(inf_g.count())}
    if len(data_selection) > len(count):
        for i in data_selection:
            if i in count:
                continue
            else:
                count[i] = 'Нет статей!'
    content_battlefield = AboutBattleField.objects.all()
    content_dungeon = AboutDungeon.objects.all()
    content_pool_of_memory = AboutPoolOfMemory.objects.all()
    content_round_table = AboutRoundTable.objects.all()
    content_main_hall = AboutMainHall.objects.all()
    dat = AboutLibrary.objects.all()

    contaxt = {
        "prTitle": "Библиотека",
        "data": dat,
        "selectGame": data_selection,
        "battlefield": content_battlefield,
        "dungeon": content_dungeon,
        "dict_count": count,
        "pool_of_memory": content_pool_of_memory,
        "round_table": content_round_table,
        "main_hall": content_main_hall,
        "this_path": request.get_full_path()
    }
    return render(request, "connects/library_cont_games.html", contaxt)


def content_games(request, name_game):
    info_game = InfoGames.objects.filter(name_games__name_game=name_game)
    content_battlefield = AboutBattleField.objects.all()
    content_dungeon = AboutDungeon.objects.all()
    content_pool_of_memory = AboutPoolOfMemory.objects.all()
    content_round_table = AboutRoundTable.objects.all()
    content_main_hall = AboutMainHall.objects.all()
    content_library = AboutLibrary.objects.all()

    contaxt = {
        "prTitle": "Библиотека",
        "pool_of_memory": content_pool_of_memory,
        "round_table": content_round_table,
        "main_hall": content_main_hall,
        "battlefield": content_battlefield,
        "dungeon": content_dungeon,
        "data": content_library,
        "name_game": name_game,
        "article_info": info_game
    }
    return render(request, "connects/library_cont_games_article.html", contaxt)


def aboutKlan(request):
    pass
