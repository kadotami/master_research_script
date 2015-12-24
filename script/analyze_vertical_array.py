# -*- coding: utf-8 -*-
########################
# tsvのverticlの配列を分析するためのプログラム
# [recipe, recipe, image]みたいな
########################

from collections import defaultdict
import datetime
from collections import Counter
from ast import literal_eval

## 年齢を計算して年代を出力
def generation_distinction(birthYear):
  if birthYear == '':
    return ''
  today = datetime.datetime.today()
  generation = (today.year - int(birthYear)) // 10
  if generation <= 1:
    return "10's"
  elif generation == 2:
    return "20's"
  elif generation == 3:
    return "30's"
  elif generation == 4:
    return "40's"
  elif generation == 5:
    return "50's"
  else:
    return "60's"

## dicの中身をソートして出力
def print_dict_content(dic):
  for v in dic:
    allNum = dic[v]["all"]
    if allNum == 0:
      continue
    print ("----------"+v+"----------")
    dic[v] = sorted(dic[v].items(), key=lambda x: x[1])
    for y in dic[v]:
      print (y[0]+','+str(y[1]) + "," + str(float(y[1])/allNum * 100) + "%")

def ave(data):
  ans = float(sum(data))/float(len(data))
  return ans

## 一番出現したverticalをリストで返す
def mostFreqVertical(li):
  if len(li) == 0:
    return []
  dic = Counter(li)
  array = []
  max_val = max(dic[x] for x in dic)
  for k, v in dic.iteritems():
    if v == max_val:
        array.append(k)
  return array

if __name__ == "__main__":
  first_allDict = {
    "all": defaultdict(lambda: 0)
  }
  first_deviceDict = {
    "pc": defaultdict(lambda: 0),
    "smartphone": defaultdict(lambda: 0),
    "tv": defaultdict(lambda: 0),
    "tablet": defaultdict(lambda: 0)
  }
  first_generationDict = {
    "10's": defaultdict(lambda: 0),
    "20's": defaultdict(lambda: 0),
    "30's": defaultdict(lambda: 0),
    "40's": defaultdict(lambda: 0),
    "50's": defaultdict(lambda: 0),
    "60's": defaultdict(lambda: 0)
  }
  first_genderDict = {
    "m": defaultdict(lambda: 0),
    "f": defaultdict(lambda: 0)
  }
  # 最初のヴァーティカルと頻出ヴァーティカルが同じ物の数
  common_allDict = {
    "all": defaultdict(lambda: 0)
  }
  common_deviceDict = {
    "pc": defaultdict(lambda: 0),
    "smartphone": defaultdict(lambda: 0),
    "tv": defaultdict(lambda: 0),
    "tablet": defaultdict(lambda: 0)
  }
  common_generationDict = {
    "10's": defaultdict(lambda: 0),
    "20's": defaultdict(lambda: 0),
    "30's": defaultdict(lambda: 0),
    "40's": defaultdict(lambda: 0),
    "50's": defaultdict(lambda: 0),
    "60's": defaultdict(lambda: 0)
  }
  common_genderDict = {
    "m": defaultdict(lambda: 0),
    "f": defaultdict(lambda: 0)
  }

  # 遷移確率を格納するdic
  transDict = {
    "image": defaultdict(lambda: 0),
    "chie": defaultdict(lambda: 0),
    "video": defaultdict(lambda: 0),
    "recipe": defaultdict(lambda: 0),
    "loco": defaultdict(lambda: 0),
    "news": defaultdict(lambda: 0),
    "shopping": defaultdict(lambda: 0),
    "auction": defaultdict(lambda: 0),
    "realtime": defaultdict(lambda: 0),
    "talent": defaultdict(lambda: 0),
    "map": defaultdict(lambda: 0),
    "dic": defaultdict(lambda: 0),
    "other": defaultdict(lambda: 0)
  }

  all_data = 0
  length_one = 0 #1つしかページを見ていないものがいくつあるか
  length_two = 0
  length_three = 0
  for line in open('../data/serp_array.txt', 'r'):
  # for line in open('../data/serp_test_data.txt', 'r'):
    featureArray = line.split("\t")
    gender = featureArray[0]
    birthYear = featureArray[1]
    generation = generation_distinction(birthYear)
    device = featureArray[2]
    verticalList = literal_eval(featureArray[3])
    # verticalが1の時を除くかどうか
    if len(verticalList) == 0:
      continue
    if len(verticalList) == 1:
      length_one += 1
    if len(verticalList) == 2:
      length_two += 1
    if len(verticalList) > 2:
      length_three += 1
    firstVirtical = verticalList[0]
    mostVerticalList = mostFreqVertical(verticalList)
    all_data += 1
    first_allDict["all"][firstVirtical] += 1
    #  各属性の最初のverticalの数
    if gender != '':
      first_genderDict[gender]["all"] += 1
      first_genderDict[gender][firstVirtical] += 1
    if generation != '':
      first_generationDict[generation]["all"] += 1
      first_generationDict[generation][firstVirtical] += 1
    if device != '':
      first_deviceDict[device]["all"] += 1
      first_deviceDict[device][firstVirtical] += 1

    # 最初のヴァーティカルと頻出するヴァーティカルが同じものを出す
    # 条件は3つ以上クリックしていてで出現回数が2以上のもの
    if len(verticalList) > 2 and len(verticalList) != len(mostVerticalList):
      if firstVirtical in mostVerticalList:
        common_allDict["all"][firstVirtical] += 1
        if gender != '':
          common_genderDict[gender][firstVirtical] += 1
        if generation != '':
          common_generationDict[generation][firstVirtical] += 1
        if device != '':
          common_deviceDict[device][firstVirtical] += 1

    # 遷移確率を求める
    if len(verticalList) > 1:
      for x in xrange(0,len(verticalList)-1):
        transDict[verticalList[x]][verticalList[x+1]] += 1
        transDict[verticalList[x]]["all"] += 1

  print all_data,length_one,length_two,length_three
  print_dict_content(first_allDict)
  print_dict_content(first_genderDict)
  print_dict_content(first_generationDict)
  print_dict_content(first_deviceDict)
  print_dict_content(common_allDict)
  print_dict_content(common_genderDict)
  print_dict_content(common_generationDict)
  print_dict_content(common_deviceDict)
  print_dict_content(transDict)
