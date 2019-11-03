from collections import defaultdict

from django.http import request
from django.shortcuts import render
from django.views import View

from BattlleField.models import AboutBattleField
from Dungeon.models import AboutDungeon
from MainHall.models import AboutMainHall
from PoolOfMemory.models import AboutPoolOfMemory
from RoundTable.models import AboutRoundTable
from .models import AboutLibrary, SectionInLibraryAboutGames, SectionInLibraryAboutKlan, ContentsInSectionGames, \
    InfoGames, ContentAboutKlan

from article.models import *


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
    count = {inf_g[i].name_games: 'Кол-во статей: ' + str(inf_g.filter(name_games=inf_g[i].name_games).count()) for i in
             range(inf_g.count())}
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
    content_about_klan = ContentAboutKlan.objects.all()
    content_battlefield = AboutBattleField.objects.all()
    content_dungeon = AboutDungeon.objects.all()
    content_pool_of_memory = AboutPoolOfMemory.objects.all()
    content_round_table = AboutRoundTable.objects.all()
    content_main_hall = AboutMainHall.objects.all()
    content_library = AboutLibrary.objects.all()

    contaxt = {
        "prTitle": "Библиотека",
        "battlefield": content_battlefield,
        "dungeon": content_dungeon,
        "pool_of_memory": content_pool_of_memory,
        "round_table": content_round_table,
        "main_hall": content_main_hall,
        "data": content_library,
        'content': content_about_klan
    }

    return render(request, 'connects/library_cont_about_klan.html', contaxt)


def article(request, name_game, name_article):
    content_dict = dict()
    data_head = HeaderConstructorArticleGames.objects.filter(name_article__slug=name_article)
    data_body = BodyConstructorArticleGame.objects.filter(name_article__slug=name_article)
    data_sub_body = SubBodyConstructorArticleGame.objects.filter(body_article__name_article__slug=name_article)
    data_content = ContentSubBodyConstructorArticleGame.objects. \
        filter(sub_name_article__body_article__name_article__slug=name_article)

    data_video_gallery = InfoCreateGalleryVideo.objects.filter(name_article__slug=name_article)
    data_image_gallery = ImageGallery.objects.filter(name_article__slug=name_article)

    context = {
        'name_game': name_game,
        'name_article': name_article,
        'name_head': data_head,
        'name_body': data_body,
        'name_sub_body': data_sub_body,
        'name_content': data_content,
        'video_gallery': data_video_gallery,
        'image_gallery': data_image_gallery,
    }
    return render(request, 'article/article.html', context)


"""
      Слишком багоая идея

      count_row = []
      count_col = []
      value_row = []
      value_col = dict()
      value_cont = []
      char_cont = []
      other_content = dict()
      dictInTable = dict()
      dictContTable = nested_dict(3, ContentCreateTable)
      dictCont = dict()
      dictCont2 = dict()

      if data.type_content == 'TABLE': 
          for row in range(data.table_content.count_row):
              for col in range(data.table_content.count_col):
                  dictInTable = dict({i.content_table.cell_text: i.content_table for i in
                                      data_table.filter(info_table=
                                                        data.table_content.pk)})
          count_row = [i + 1 for i in range(data.table_content.count_row)]
          count_col = [i + 1 for i in range(data.table_content.count_col)]
          for key, count in dictInTable.items():
              if count.number_col > len(count_col):
                  other_content.update({key: count})

          for row in count_row:
              for col in count_col:
                  for key, value in dictInTable.items():
                      if value.number_row == row:
                          if value.number_col == col:
                              dictContTable[row][col][key] = value
              if other_content:
                  for key, value in other_content.items():
                      if value.number_row == row:
                          dictContTable[row][value.number_col][key] = value
          for key in dictContTable.keys():
              value_row.append(key)
              value_col.update({key: []})
              for col in dictContTable[key].keys():
                  if col > len(count_col):
                      pass
                  else:
                      value_col[key].append(col)
                  for key2, value2 in dictContTable[key][col].items():
                      if value2.number_col > len(count_col):
                          dictCont2.update({key2: value2})
                      else:
                          dictCont.update({key2: value2})
      if data.type_content == "LIST":
          pass"""
