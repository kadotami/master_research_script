# -*- coding: utf-8 -*-
########################
# 男女で1セッション中にみるverticalの種類、ページの数を分析
########################

from collections import defaultdict
import datetime
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
  if len(data) == 0:
    return 0
  ans = float(sum(data))/float(len(data))
  return ans

if __name__ == "__main__":
  dic = {
    "m": {
      "length": [],
      "kind": [],
    },
    "f": {
      "length": [],
      "kind": [],
    },
    "smartphone": {
      "length": [],
      "kind": [],
    },
    "tablet": {
      "length": [],
      "kind": [],
    },
    "pc": {
      "length": [],
      "kind": [],
    },
    "tv": {
      "length": [],
      "kind": [],
    },
    "10's": {
      "length": [],
      "kind": [],
    },
    "20's": {
      "length": [],
      "kind": [],
    },
    "30's": {
      "length": [],
      "kind": [],
    },
    "40's": {
      "length": [],
      "kind": [],
    },
    "50's": {
      "length": [],
      "kind": [],
    },
    "60's": {
      "length": [],
      "kind": [],
    },
  }

  len_dic = {
    "m": defaultdict(lambda: 0),
    "f": defaultdict(lambda: 0),
    "10's": defaultdict(lambda: 0),
    "20's": defaultdict(lambda: 0),
    "30's": defaultdict(lambda: 0),
    "40's": defaultdict(lambda: 0),
    "50's": defaultdict(lambda: 0),
    "60's": defaultdict(lambda: 0),
    "pc": defaultdict(lambda: 0),
    "tablet": defaultdict(lambda: 0),
    "smartphone": defaultdict(lambda: 0),
    "tv": defaultdict(lambda: 0),
  }
  all_data = 0
  length_one = 0 #1つしかページを見ていないものがいくつあるか
  length_two_more = 0
  for line in open('../data/serp_array.txt', 'r'):
  #for line in open('../data/session_array_30min.txt', 'r'):
  # for line in open('../data/session_data.txt', 'r'):
    featureArray = line.split("\t")
    gender = featureArray[0]
    birthYear = featureArray[1]
    generation = generation_distinction(birthYear)
    device = featureArray[2]
    verticalList = literal_eval(featureArray[3])
    # verticalが1の時を除くかどうか
    all_data += 1
    if len(verticalList) == 0:
      continue
    elif len(verticalList) == 1:
      length_one += 1
      if gender != '':
        len_dic[gender][str(len(verticalList))] += 1
        len_dic[gender]["all"] += 1
      if birthYear != '':
        len_dic[generation][str(len(verticalList))] += 1
        len_dic[generation]["all"] += 1
      if device != '':
        len_dic[device][str(len(verticalList))] += 1
        len_dic[device]["all"] += 1
      continue
    else:
      length_two_more += 1
      if gender != '':
        dic[gender]["length"].append(len(verticalList))
        dic[gender]["kind"].append(len(list(set(verticalList))))
        len_dic[gender][str(len(verticalList))] += 1
        len_dic[gender]["all"] += 1
      if birthYear != '':
        dic[generation]["length"].append(len(verticalList))
        dic[generation]["kind"].append(len(list(set(verticalList))))
        len_dic[generation][str(len(verticalList))] += 1
        len_dic[generation]["all"] += 1
      if device != '':
        dic[device]["length"].append(len(verticalList))
        dic[device]["kind"].append(len(list(set(verticalList))))
        len_dic[device][str(len(verticalList))] += 1
        len_dic[device]["all"] += 1

  print length_one, all_data
  print "======= gender ======="
  print ave(dic["m"]["length"]),ave(dic["m"]["kind"])
  print ave(dic["f"]["length"]),ave(dic["f"]["kind"])

  print "======= generation ======="
  print ave(dic["10's"]["length"]),ave(dic["10's"]["kind"])
  print ave(dic["20's"]["length"]),ave(dic["20's"]["kind"])
  print ave(dic["30's"]["length"]),ave(dic["30's"]["kind"])
  print ave(dic["40's"]["length"]),ave(dic["40's"]["kind"])
  print ave(dic["50's"]["length"]),ave(dic["50's"]["kind"])
  print ave(dic["60's"]["length"]),ave(dic["60's"]["kind"])

  print "======= device ======="
  print ave(dic["pc"]["length"]),ave(dic["pc"]["kind"])
  print ave(dic["tablet"]["length"]),ave(dic["tablet"]["kind"])
  print ave(dic["smartphone"]["length"]),ave(dic["smartphone"]["kind"])

  print_dict_content(len_dic)