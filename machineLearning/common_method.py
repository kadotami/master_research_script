# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import jholiday

def generation_distinction(birthYear):
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
      return 0
    print ("----------"+v+"----------")
    dic[v] = sorted(dic[v].items(), key=lambda x: x[1])
    for y in dic[v]:
      print (y[0]+','+str(y[1]) + "," + str(float(y[1])/allNum * 100) + "%")

## verticalを大きなまとめに
def typical_vertical(vertical):
  if vertical in ["isrch", "isearch", "bigimage"]:
    return "image"
  elif vertical in ["vsrch", "vsearch", "gvideo", "movie", "mvrnk", "drama", "tv", "tvrank"]:
    return "video"
  elif vertical in ["dic", "kb", "wiki"]:
    return "dic"
  elif vertical in ["chie"]:
    return "chie"
  elif vertical in ["map", "maps", "tv-spot"]:
    return "map"
  elif vertical in ["realtime", "rts", "buzz", "bzw"]:
    return "realtime"
  elif vertical in ["news"]:
    return "news"
  elif vertical in ["shp", "cmcnb", "shpkw", "shprank", "cmcat", "fashion", "dcomic", "store", "adcomic"]:
    return "shopping"
  elif vertical in ["auc", "auction"]:
    return "auction"
  elif vertical in ["talent", "tlnt", "psnsp", "avtlnt"]:
    return "talent"
  elif vertical in ["recipe", "rcp", "cookpad", "hrecipe"]:
    return "recipe"
  elif vertical in ["loco", "local", "iplocal"]:
    return "loco"
  else:
    return "other"

def is_holiday(date):#datetime型で引数を取る
  if jholiday.holiday_name(date.year,date.month,date.day) is not None or date.weekday() > 5:
    return True
  return False


def unix2hour(unixtime):
  return str(datetime.datetime.fromtimestamp(unixtime).hour)

def unix2date(unixtime):
  return str(datetime.datetime.fromtimestamp(unixtime).strftime("%Y%m%d"))

def label2id(label):
  if label == "image":
    return 1
  elif label == "video":
    return 2
  elif label == "dic":
    return 3
  elif label == "chie":
    return 4
  elif label == "map":
    return 5
  elif label == "realtime":
    return 6
  elif label == "news":
    return 7
  elif label == "shopping":
    return 8
  elif label == "auction":
    return 9
  elif label == "talent":
    return 10
  elif label == "recipe":
    return 11
  elif label == "loco":
    return 12

def id2label(id):
  if id == 1:
    return "image"
  elif id == 2:
    return "video"
  elif id == 3:
    return "dic"
  elif id == 4:
    return "chie"
  elif id == 5:
    return "map"
  elif id == 6:
    return "realtime"
  elif id == 7:
    return "news"
  elif id == 8:
    return "shopping"
  elif id == 9:
    return "auction"
  elif id == 10:
    return "talent"
  elif id == 11:
    return "recipe"
  elif id == 12:
    return "loco"
