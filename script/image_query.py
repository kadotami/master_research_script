# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import re
import common_method as cm

#
# 「画像」がクエリに含まれていた場合のvertical
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
    "「レシピ」なし": defaultdict(lambda: 0)
  }
  img_rexp = re.compile(r'.*%s.*' % "画像")
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
  print_dict_content(result)
