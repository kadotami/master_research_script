# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import common_method as cm

#########################################
# imageの利用率を算出
#########################################

if __name__ == "__main__":
  analyzeVertical = []
  allDict = {
    "all":defaultdict(lambda: 0)
  }
  deviceDict = {
    "pc": defaultdict(lambda: 0),
    "smartphone": defaultdict(lambda: 0),
    "tv": defaultdict(lambda: 0),
    "tablet": defaultdict(lambda: 0),
    "featurephone": defaultdict(lambda: 0),
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

  # 全部複合の辞書
  detailDict = {
    "10's": {
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0)
    },
    "20's": {
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0)
    },
    "30's": {
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0)
    },
    "40's": {
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0)
    },
    "50's": {
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0)
    },
    "60's": {
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0)
    },
  }

  outputs = {
    "device": {},
    "gender": {},
    "generation": {}
  }

  other_verical_array = []

  for fileNum in xrange(2,9):
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
    # for line in open('../data/small_data.txt', 'r'):
      featureArray = line.split("\t")
      vertical = cm.typical_vertical(featureArray[10])
      if vertical != "talent":
        continue
      device = featureArray[8]
      if vertical == "other" and featureArray[10] not in other_verical_array:
        other_verical_array.append(featureArray[10])
      birthYear = featureArray[2]
      gender = featureArray[1]
        # vertical = "None"
      allDict["all"]["all"] += 1

      if birthYear != "" and gender != "" and device in ["smartphone", "tablet", "pc", "tv", "featurephone"]:
        generation = cm.generation_distinction(birthYear)
        generationDict[generation]["all"] += 1
        generationDict[generation][vertical] += 1
        genderDict[gender]["all"] += 1
        genderDict[gender][vertical] += 1
        deviceDict[device]["all"] += 1
        deviceDict[device][vertical] += 1
        detailDict[generation][gender][device] += 1

  for gene in ["10's","20's","30's","40's","50's","60's"]:
    try:
      print str(detailDict[gene]["m"]["smartphone"])+","+str(detailDict[gene]["m"]["tablet"])+","+str(detailDict[gene]["m"]["pc"])+","+str(detailDict[gene]["f"]["smartphone"])+","+str(detailDict[gene]["f"]["tablet"])+","+str(detailDict[gene]["f"]["pc"])
    except Exception, e:
      pass

  print "----------------------------------------------"
  for gene in ["10's","20's","30's","40's","50's","60's"]:
    try:
      print str(float(detailDict[gene]["m"]["smartphone"])/allDict["all"]["all"]*100)+"%,"+str(float(detailDict[gene]["m"]["tablet"])/allDict["all"]["all"]*100)+"%,"+str(float(detailDict[gene]["m"]["pc"])/allDict["all"]["all"]*100)+"%,"+str(float(detailDict[gene]["f"]["smartphone"])/allDict["all"]["all"]*100)+"%,"+str(float(detailDict[gene]["f"]["tablet"])/allDict["all"]["all"]*100)+"%,"+str(float(detailDict[gene]["f"]["pc"])/allDict["all"]["all"]*100) + "%"
    except Exception, e:
      pass