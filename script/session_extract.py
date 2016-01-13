# -*- coding: utf-8 -*-
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

## 一番出現したverticalをリストで返す
def mostFreqVertical(dict):
  if dict == {}:
    return []
  array = []
  max_val = max(dict[x] for x in dict)
  for k, v in dict.iteritems():
    if v == max_val:
        array.append(k)
  return array

if __name__ == "__main__":
  prevBrowserId = ""
  prevSearchTime = ""
  prevClickTime = ""
  sessionTerm = 1800
  sessionVertical = defaultdict(lambda: 0)
  prevVertical = ""
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

  for fileNum in xrange(2,9):
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
      featureArray = line.split("\t")
      if featureArray[11] != "":
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
            sessionVertical[vertical] += 1
          ##30分以内に動作があれば同じセッション
          elif (int(prevClickTime) - int(searchTime)) > 0 and (int(prevClickTime) - int(searchTime)) <= sessionTerm:
            sessionVertical[vertical] += 1
          ## この行は前の行とセッション違う
          else:
            verticalList = mostFreqVertical(sessionVertical)
            for vertical in verticalList:
              allDict["all"]["all"] += 1
              allDict["all"][vertical] += 1
              if birthYear != "":
                generation = generation_distinction(birthYear)
                generationDict[generation]["all"] += 1
                generationDict[generation][vertical] += 1

              if gender != "":
                genderDict[gender]["all"] += 1
                genderDict[gender][vertical] += 1

              if device in ["smartphone", "tablet", "pc", "tv"]:
                deviceDict[device]["all"] += 1
                deviceDict[device][vertical] += 1

            sessionVertical = defaultdict(lambda: 0)
            sessionVertical[vertical] += 1
        ## この行は前の行とセッション違う
        else:
          verticalList = mostFreqVertical(sessionVertical)
          for vertical in verticalList:
            allDict["all"]["all"] += 1
            allDict["all"][vertical] += 1
            if birthYear != "":
              generation = generation_distinction(birthYear)
              generationDict[generation]["all"] += 1
              generationDict[generation][vertical] += 1

            if gender != "":
              genderDict[gender]["all"] += 1
              genderDict[gender][vertical] += 1

            if device in ["smartphone", "tablet", "pc", "tv", "featurephone"]:
              deviceDict[device]["all"] += 1
              deviceDict[device][vertical] += 1

          sessionVertical = defaultdict(lambda: 0)
          sessionVertical[vertical] += 1
        prevClickTime = clickTime
        prevSearchTime = searchTime
        prevBrowserId = browserId
    ## ファイルの最後
    verticalList = mostFreqVertical(sessionVertical)
    for vertical in verticalList:
      allDict["all"]["all"] += 1
      allDict["all"][vertical] += 1
      if birthYear != "":
        generation = generation_distinction(birthYear)
        generationDict[generation]["all"] += 1
        generationDict[generation][vertical] += 1

      if gender != "":
        genderDict[gender]["all"] += 1
        genderDict[gender][vertical] += 1

      if device in ["smartphone", "tablet", "pc", "tv", "featurephone"]:
        deviceDict[device]["all"] += 1
        deviceDict[device][vertical] += 1
    sessionVertical = defaultdict(lambda: 0)
    prevClickTime = 0
    prevSearchTime = 0

  print_dict_content(allDict)
  print_dict_content(deviceDict)
  print_dict_content(generationDict)
  print_dict_content(genderDict)