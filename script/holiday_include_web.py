# -*- coding: utf-8 -*-
from collections import defaultdict
from datetime import datetime
import common_method as cm

#########################################
# vertical情報が入っていなくても抽出してカウント
#########################################

if __name__ == "__main__":
  analyzeVertical = []
  allDict = {
    "all":defaultdict(lambda: 0)
  }

  # 全部複合の辞書
  holi_detailDict = {
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
  week_detailDict = {
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
    date = '2015110'+str(fileNum)
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
    # for line in open('../data/small_data.txt', 'r'):
      is_holiday = cm.is_holiday(datetime.strptime(date,"%Y%m%d"))
      featureArray = line.split("\t")
      # if featureArray[11] != "":
        # if featureArray[10] == "":
        #   continue
      browseId = featureArray[0]
      device = featureArray[8]
      vertical = cm.typical_vertical(featureArray[10])
      if vertical == "other" and featureArray[10] not in other_verical_array:
        other_verical_array.append(featureArray[10])
      birthYear = featureArray[2]
      gender = featureArray[1]
        # vertical = "None"
      allDict["all"]["all"] += 1
      allDict["all"][vertical] += 1

      if birthYear != "" and gender != "" and device in ["smartphone", "tablet", "pc", "tv", "featurephone"]:
        generation = cm.generation_distinction(birthYear)
        if is_holiday:
          holi_detailDict[generation][gender][device] += 1
        else:
          week_detailDict[generation][gender][device] += 1

  print "=========other vertical=========="
  print str(other_verical_array)
  print "================================="

  print "==============holi==============="
  for gene in ["10's","20's","30's","40's","50's","60's"]:
    for gen in ["m","f"]:
      for devi in ["smartphone", "tablet", "pc", "tv", "featurephone"]:
        try:
          print gene +": "+ gen+": " + devi
          print holi_detailDict[gene][gen][devi]
        except Exception, e:
          pass

  print "==============week==============="
  for gene in ["10's","20's","30's","40's","50's","60's"]:
    for gen in ["m","f"]:
      for devi in ["smartphone", "tablet", "pc", "tv", "featurephone"]:
        try:
          print gene +": "+ gen+": " + devi
          print week_detailDict[gene][gen][devi]
        except Exception, e:
          pass