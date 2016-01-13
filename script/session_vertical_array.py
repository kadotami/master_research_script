# -*- coding: utf-8 -*-
########################
# セッションごとのverticalが順番に入った配列を返す
# [recipe, recipe, image]みたいな
########################

from collections import defaultdict
import datetime

## 年齢を計算して年代を出力
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
      continue
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
  elif vertical in ["realtime", "rts", "buzz"]:
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

if __name__ == "__main__":
  allDict = {
    "all": defaultdict(lambda: 0)
  }
  deviceDict = {
    "pc": defaultdict(lambda: 0),
    "smartphone": defaultdict(lambda: 0),
    "tv": defaultdict(lambda: 0),
    "tablet": defaultdict(lambda: 0)
  }
  generationDict = {
    "10's": defaultdict(lambda: 0),
    "20's": defaultdict(lambda: 0),
    "30's": defaultdict(lambda: 0),
    "40's": defaultdict(lambda: 0),
    "50's": defaultdict(lambda: 0),
    "60's": defaultdict(lambda: 0)
  }
  genderDict = {
    "m": defaultdict(lambda: 0),
    "f": defaultdict(lambda: 0)
  }

  outputs = {
    "device": {},
    "gender": {},
    "generation": {}
  }
  allSessionArray = []
  prevBrowserId = ""
  prevSearchTime = 0
  prevClickTime = 0
  sessionTerm = 1800
  sessionVerticalArray = []
  prevVertical = ""

  for fileNum in xrange(2,9):
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
    # for line in open('../data/small_data.txt','r'):
      featureArray = line.split("\t")
      # if featureArray[11] != "":
      if featureArray[10] == "":
        continue
      browserId = featureArray[0]
      gender = featureArray[1]
      birthYear = featureArray[2]
      searchTime = featureArray[5].split(",")[0]
      device = featureArray[8]
      vertical = typical_vertical(featureArray[10])
      clickTime = featureArray[12].split(",")[0]

      if browserId == prevBrowserId:
        ##　検索時間が同じなら同じセッション
        if searchTime == prevSearchTime:
          sessionVerticalArray.append(vertical)
          prevClickTime = clickTime
          prevSearchTime = searchTime
        ##30分以内に動作があれば同じセッション
        elif (int(prevClickTime) - int(searchTime)) > 0 and (int(prevClickTime) - int(searchTime)) <= sessionTerm:
          sessionVerticalArray.append(vertical)
          prevClickTime = clickTime
          prevSearchTime = searchTime
        else:
          allSessionArray.append(sessionVerticalArray)
          print str(gender)+"\t"+str(birthYear)+"\t"+str(device)+"\t"+str(sessionVerticalArray)
          sessionVerticalArray = []
          sessionVerticalArray.append(vertical)
          prevClickTime = clickTime
          prevSearchTime = searchTime
        prevBrowserId = browserId
      else:
        allSessionArray.append(sessionVerticalArray)
        print str(gender)+"\t"+str(birthYear)+"\t"+str(device)+"\t"+str(sessionVerticalArray)
        sessionVerticalArray = []
        sessionVerticalArray.append(vertical)
        prevClickTime = clickTime
        prevSearchTime = searchTime
        prevBrowserId = browserId

    ## ファイルの最後
    allSessionArray.append(sessionVerticalArray)
    print str(gender)+"\t"+str(birthYear)+"\t"+str(device)+"\t"+str(sessionVerticalArray)
    sessionVerticalArray = []
    sessionVerticalArray.append(vertical)
    prevClickTime = ""
    prevSearchTime = ""

  # sessionOneQuery = defaultdict(lambda: 0)
  # sessionDict = {
  #   "image": defaultdict(lambda: 0),
  #   "chie": defaultdict(lambda: 0),
  #   "video": defaultdict(lambda: 0),
  #   "recipe": defaultdict(lambda: 0),
  #   "loco": defaultdict(lambda: 0),
  #   "news": defaultdict(lambda: 0),
  #   "shopping": defaultdict(lambda: 0),
  #   "auction": defaultdict(lambda: 0),
  #   "realtime": defaultdict(lambda: 0),
  #   "talent": defaultdict(lambda: 0),
  #   "map": defaultdict(lambda: 0),
  #   "dic": defaultdict(lambda: 0),
  #   "other": defaultdict(lambda: 0)
  # }
  # for array in allSessionArray:
  #   if len(array) < 1:
  #     continue
  #   elif len(array) < 2:
  #     sessionOneQuery[array[0]] += 1
  #     continue
  #   for x in xrange(0,len(array)-1):
  #     sessionDict[array[x]][array[x+1]] += 1
  #     sessionDict[array[x]]["all"] += 1
  # print_dict_content(sessionDict)