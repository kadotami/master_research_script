# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import re
import common_method as cm

#
# クエリにヴァーティカルを表す語が含まれている割合
#

## dicの中身をソートして出力
def print_dict_content(dic):
  for v in dic:
    allNum = dic[v]["all"]
    print ("----------"+v+"----------")
    dic[v] = sorted(dic[v].items(), key=lambda x: x[1])
    for y in dic[v]:
      print (y[0]+','+str(y[1]) + "," + str(float(y[1])/allNum * 100) + "%")

if __name__ == "__main__":
  result = {
    "「画像」あり": defaultdict(lambda: 0),
    "「画像」なし": defaultdict(lambda: 0),
    "「レシピ」あり": defaultdict(lambda: 0),
    "「レシピ」なし": defaultdict(lambda: 0),
    "「動画」あり": defaultdict(lambda: 0),
    "「動画」なし": defaultdict(lambda: 0),
    "「ニュース」あり": defaultdict(lambda: 0),
    "「ニュース」なし": defaultdict(lambda: 0),
    "「地図」あり": defaultdict(lambda: 0),
    "「地図」なし": defaultdict(lambda: 0),
    "「知恵袋」あり": defaultdict(lambda: 0),
    "「知恵袋」なし": defaultdict(lambda: 0)
  }
  img_rexp = re.compile(r'.*%s.*' % "画像")
  video_rexp = re.compile(r'.*%s.*' % "動画")
  map_rexp = re.compile(r'.*%s.*' % "地図")
  chie_rexp = re.compile(r'.*%s.*' % "知恵袋")
  news_rexp = re.compile(r'.*%s.*' % "ニュース")
  recipe_rexp = [re.compile(r'.*%s.*' % "クックパッド"), re.compile(r'.*%s.*' % "レシピ")]
  for fileNum in xrange(2,9):
    # for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
    for line in open('../data/small_data.txt', 'r'):
      featureArray = line.split("\t")
      # if featureArray[11] == "":
      #   continue
      if cm.typical_vertical(featureArray[10]) == "image":
        if img_rexp.match(featureArray[7]):
          result["「画像」あり"][featureArray[10]] += 1
          result["「画像」あり"]["all"] += 1
        else:
          result["「画像」なし"][featureArray[10]] += 1
          result["「画像」なし"]["all"] += 1
      elif cm.typical_vertical(featureArray[10]) == "recipe":
        if recipe_rexp[0].match(featureArray[7]) or recipe_rexp[1].match(featureArray[7]):
          result["「レシピ」あり"][featureArray[10]] += 1
          result["「レシピ」あり"]["all"] += 1
        else:
          result["「レシピ」なし"][featureArray[10]] += 1
          result["「レシピ」なし"]["all"] += 1
      elif cm.typical_vertical(featureArray[10]) == "video":
        if video_rexp[0].match(featureArray[7]):
          result["「動画」あり"][featureArray[10]] += 1
          result["「動画」あり"]["all"] += 1
        else:
          result["「動画」なし"][featureArray[10]] += 1
          result["「動画」なし"]["all"] += 1
      elif cm.typical_vertical(featureArray[10]) == "news":
        if news_rexp[0].match(featureArray[7]):
          result["「ニュース」あり"][featureArray[10]] += 1
          result["「ニュース」あり"]["all"] += 1
        else:
          result["「ニュース」なし"][featureArray[10]] += 1
          result["「ニュース」なし"]["all"] += 1
      elif cm.typical_vertical(featureArray[10]) == "chie":
        if chie_rexp[0].match(featureArray[7]):
          result["「知恵袋」あり"][featureArray[10]] += 1
          result["「知恵袋」あり"]["all"] += 1
        else:
          result["「知恵袋」なし"][featureArray[10]] += 1
          result["「知恵袋」なし"]["all"] += 1
      elif cm.typical_vertical(featureArray[10]) == "map":
        if map_rexp[0].match(featureArray[7]):
          result["「地図」あり"][featureArray[10]] += 1
          result["「地図」あり"]["all"] += 1
        else:
          result["「地図」なし"][featureArray[10]] += 1
          result["「地図」なし"]["all"] += 1
  print_dict_content(result)
