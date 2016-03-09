# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
from datetime import datetime
import common_method as cm
import MeCab
import math
reload(sys)
sys.setdefaultencoding('utf-8')

##################################
#
#      時間毎に割合というか数を出してみる
#################################
if __name__ == '__main__':
  dic = {
    "all": {
      "all": defaultdict(lambda: 0),
      "smartphone": defaultdict(lambda: 0),
      "tablet": defaultdict(lambda: 0),
      "pc": defaultdict(lambda: 0),
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0),
      "10's": defaultdict(lambda: 0),
      "20's": defaultdict(lambda: 0),
      "30's": defaultdict(lambda: 0),
      "40's": defaultdict(lambda: 0),
      "50's": defaultdict(lambda: 0),
      "60's": defaultdict(lambda: 0),
      "image": defaultdict(lambda: 0),
      "video": defaultdict(lambda: 0),
      "dic": defaultdict(lambda: 0),
      "chie": defaultdict(lambda: 0),
      "map": defaultdict(lambda: 0),
      "realtime": defaultdict(lambda: 0),
      "news": defaultdict(lambda: 0),
      "shopping": defaultdict(lambda: 0),
      "auction": defaultdict(lambda: 0),
      "talent": defaultdict(lambda: 0),
      "recipe": defaultdict(lambda: 0),
      "loco": defaultdict(lambda: 0)
    },
    "holi": {
      "all": defaultdict(lambda: 0),
      "smartphone": defaultdict(lambda: 0),
      "tablet": defaultdict(lambda: 0),
      "pc": defaultdict(lambda: 0),
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0),
      "10's": defaultdict(lambda: 0),
      "20's": defaultdict(lambda: 0),
      "30's": defaultdict(lambda: 0),
      "40's": defaultdict(lambda: 0),
      "50's": defaultdict(lambda: 0),
      "60's": defaultdict(lambda: 0),
      "image": defaultdict(lambda: 0),
      "video": defaultdict(lambda: 0),
      "dic": defaultdict(lambda: 0),
      "chie": defaultdict(lambda: 0),
      "map": defaultdict(lambda: 0),
      "realtime": defaultdict(lambda: 0),
      "news": defaultdict(lambda: 0),
      "shopping": defaultdict(lambda: 0),
      "auction": defaultdict(lambda: 0),
      "talent": defaultdict(lambda: 0),
      "recipe": defaultdict(lambda: 0),
      "loco": defaultdict(lambda: 0)
    },
    "week": {
      "all": defaultdict(lambda: 0),
      "smartphone": defaultdict(lambda: 0),
      "tablet": defaultdict(lambda: 0),
      "pc": defaultdict(lambda: 0),
      "m": defaultdict(lambda: 0),
      "f": defaultdict(lambda: 0),
      "10's": defaultdict(lambda: 0),
      "20's": defaultdict(lambda: 0),
      "30's": defaultdict(lambda: 0),
      "40's": defaultdict(lambda: 0),
      "50's": defaultdict(lambda: 0),
      "60's": defaultdict(lambda: 0),
      "image": defaultdict(lambda: 0),
      "video": defaultdict(lambda: 0),
      "dic": defaultdict(lambda: 0),
      "chie": defaultdict(lambda: 0),
      "map": defaultdict(lambda: 0),
      "realtime": defaultdict(lambda: 0),
      "news": defaultdict(lambda: 0),
      "shopping": defaultdict(lambda: 0),
      "auction": defaultdict(lambda: 0),
      "talent": defaultdict(lambda: 0),
      "recipe": defaultdict(lambda: 0),
      "loco": defaultdict(lambda: 0)
    }
  }

  for fileNum in xrange(2,9):
    date = '2015110'+str(fileNum)
    for line in open('../data/'+str(date)+'_all', 'r'):
      featureArray = line.split("\t")
      vertical = cm.typical_vertical(featureArray[10])
      if vertical != "loco":
        continue
      gender = featureArray[1]
      birthYear = featureArray[2]
      query = featureArray[7].replace('　', ' ')
      searchTime = featureArray[5].split(",")[0]
      device = featureArray[8]
      clickTime = featureArray[12].split(",")[0]
      week = "week"
      if cm.is_holiday(datetime.strptime(date,"%Y%m%d")):
        week = "holi"
      hour = cm.unix2hour(float(searchTime))
      dic["all"]["all"]["all"] += 1
      dic["all"]["all"][hour] += 1
      dic[week]["all"]["all"] += 1
      dic[week]["all"][hour] += 1
      if device in ["smartphone", "tablet", "pc"]:
        dic["all"][device]["all"] += 1
        dic["all"][device][hour] += 1
        dic[week][device][hour] += 1
        dic[week][device]["all"] += 1
      if gender != "":
        dic[week][gender][hour] += 1
        dic[week][gender]["all"] += 1
        dic["all"][gender][hour] += 1
        dic["all"][gender]["all"] += 1
      if birthYear != "":
        generation = cm.generation_distinction(birthYear)
        dic["all"][generation][hour] += 1
        dic["all"][generation]["all"] += 1
        dic[week][generation][hour] += 1
        dic[week][generation]["all"] += 1
      if vertical != "other":
        dic[week][vertical][hour] += 1
        dic[week][vertical]["all"] += 1
        dic["all"][vertical][hour] += 1
        dic["all"][vertical]["all"] += 1

  print "======================================="
  print "=============     all     ============="
  print "======================================="
  cm.print_dict_content(dic["all"])

  print "======================================="
  print "==========     weekday     ============"
  print "======================================="
  cm.print_dict_content(dic["week"])

  print "======================================="
  print "==========     holiday     ============"
  print "======================================="
  cm.print_dict_content(dic["holi"])
