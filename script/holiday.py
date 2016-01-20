# -*- coding: utf-8 -*-
from collections import defaultdict
from datetime import datetime
import common_method as cm

#########################################
# vertical情報が入っているものだけを抽出
#########################################

if __name__ == "__main__":
  analyzeVertical = []
  weekdayDict = {
    "allDict": {
      "all":defaultdict(lambda: 0)
    },
    "deviceDict": {
      "pc": defaultdict(lambda: 0),
      "smartphone": defaultdict(lambda: 0),
      "tv": defaultdict(lambda: 0),
      "tablet": defaultdict(lambda: 0),
      "featurephone": defaultdict(lambda: 0),
    },
    "generationDict": {
      "10's": defaultdict(lambda: 0),
      "20's": defaultdict(lambda: 0),
      "30's": defaultdict(lambda: 0),
      "40's": defaultdict(lambda: 0),
      "50's": defaultdict(lambda: 0),
      "60's": defaultdict(lambda: 0)
    },
    "genderDict": {
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0)
    }
  }
  holidayDict = {
    "allDict": {
      "all":defaultdict(lambda: 0)
    },
    "deviceDict": {
      "pc": defaultdict(lambda: 0),
      "smartphone": defaultdict(lambda: 0),
      "tv": defaultdict(lambda: 0),
      "tablet": defaultdict(lambda: 0),
      "featurephone": defaultdict(lambda: 0),
    },
    "generationDict": {
      "10's": defaultdict(lambda: 0),
      "20's": defaultdict(lambda: 0),
      "30's": defaultdict(lambda: 0),
      "40's": defaultdict(lambda: 0),
      "50's": defaultdict(lambda: 0),
      "60's": defaultdict(lambda: 0)
    },
    "genderDict": {
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0)
    }
  }

  other_verical_array = []
  other_device = []

  for fileNum in xrange(2,9):
    date = '2015110'+str(fileNum)
    for line in open('../data/'+str(date)+'_all', 'r'):
      is_holiday = cm.is_holiday(datetime.strptime(date,"%Y%m%d"))
      featureArray = line.split("\t")
      # if featureArray[11] != "":
      if featureArray[10] == "":
        continue
      browseId = featureArray[0]
      device = featureArray[8]
      vertical = cm.typical_vertical(featureArray[10])
      if vertical == "other" and featureArray[10] not in other_verical_array:
        other_verical_array.append(featureArray[10])
      birthYear = featureArray[2]
      gender = featureArray[1]

      if birthYear != "" and gender != "" and device in ["smartphone", "tablet", "pc", "tv", "featurephone"]:
        if is_holiday:
          generation = cm.generation_distinction(birthYear)
          holidayDict["generationDict"][generation]["all"] += 1
          holidayDict["generationDict"][generation][vertical] += 1
          holidayDict["deviceDict"][device]["all"] += 1
          holidayDict["deviceDict"][device][vertical] += 1
          holidayDict["genderDict"][gender]["all"] += 1
          holidayDict["genderDict"][gender][vertical] += 1
        else:
          generation = cm.generation_distinction(birthYear)
          weekdayDict["generationDict"][generation]["all"] += 1
          weekdayDict["generationDict"][generation][vertical] += 1
          weekdayDict["deviceDict"][device]["all"] += 1
          weekdayDict["deviceDict"][device][vertical] += 1
          weekdayDict["genderDict"][gender]["all"] += 1
          weekdayDict["genderDict"][gender][vertical] += 1

  cm.print_dict_content(weekdayDict["allDict"])
  cm.print_dict_content(weekdayDict["deviceDict"])
  cm.print_dict_content(weekdayDict["generationDict"])
  cm.print_dict_content(weekdayDict["genderDict"])
  cm.print_dict_content(holidayDict["allDict"])
  cm.print_dict_content(holidayDict["deviceDict"])
  cm.print_dict_content(holidayDict["generationDict"])
  cm.print_dict_content(holidayDict["genderDict"])

  print "===========other============"
  for x in other_device:
    print x