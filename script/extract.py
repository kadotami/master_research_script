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
  analyzeVertical = []
  allDict = {
    "all":defaultdict(lambda: 0)
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
  outputs["device"]["smartphone"] = open('/vgca/shared/c-yukadotami/data/device/smartphone.txt', "w")
  outputs["device"]["pc"] = open('/vgca/shared/c-yukadotami/data/device/pc.txt', "w")
  outputs["device"]["tablet"] = open('/vgca/shared/c-yukadotami/data/device/tablet.txt', "w")
  outputs["device"]["tv"] = open('/vgca/shared/c-yukadotami/data/device/tv.txt', "w")
  outputs["gender"]["m"] = open('/vgca/shared/c-yukadotami/data/gender/male.txt', "w")
  outputs["gender"]["f"] = open('/vgca/shared/c-yukadotami/data/gender/female.txt', "w")
  outputs["generation"]["10's"] = open('/vgca/shared/c-yukadotami/data/generation/10s.txt', "w")
  outputs["generation"]["20's"] = open('/vgca/shared/c-yukadotami/data/generation/20s.txt', "w")
  outputs["generation"]["30's"] = open('/vgca/shared/c-yukadotami/data/generation/30s.txt', "w")
  outputs["generation"]["40's"] = open('/vgca/shared/c-yukadotami/data/generation/40s.txt', "w")
  outputs["generation"]["50's"] = open('/vgca/shared/c-yukadotami/data/generation/50s.txt', "w")
  outputs["generation"]["60's"] = open('/vgca/shared/c-yukadotami/data/generation/60s.txt', "w")

  for fileNum in xrange(2,9):
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
      featureArray = line.split("\t")
      if featureArray[11] != "":
        if featureArray[10] == "":
          continue
        browseId = featureArray[0]
        device = featureArray[8]
        vertical = typical_vertical(featureArray[10])
        birthYear = featureArray[2]
        gender = featureArray[1]
          # vertical = "None"
        allDict["all"]["all"] += 1
        allDict["all"][vertical] += 1
        if birthYear != "":
          generation = generation_distinction(birthYear)
          generationDict[generation]["all"] += 1
          generationDict[generation][vertical] += 1
          outputs["generation"][generation].write(line)

        if gender != "":
          genderDict[gender]["all"] += 1
          genderDict[gender][vertical] += 1
          outputs["gender"][gender].write(line)

        if device in ["smartphone", "tablet", "pc", "tv"]:
          deviceDict[device]["all"] += 1
          deviceDict[device][vertical] += 1
          outputs["device"][device].write(line)
        else:
          other_device.push(device)

  print_dict_content(allDict)
  print_dict_content(deviceDict)
  print_dict_content(generationDict)
  print_dict_content(genderDict)