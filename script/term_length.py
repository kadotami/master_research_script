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
#   クエリの単語数による差
#################################

def print_dict_content(dic):
  for v in dic:
    print ("----------"+v+"----------")
    dic[v] = sorted(dic[v].items(), key=lambda x: x[1])
    for y in dic[v]:
      print (y[0]+','+str(y[1]) + ",")


if __name__ == '__main__':
  dic = {
    "all": {"all": 0},
    "1": defaultdict(lambda: 0),
    "2": defaultdict(lambda: 0),
    "3": defaultdict(lambda: 0),
    "4": defaultdict(lambda: 0),
    "5": defaultdict(lambda: 0)
  }

  for fileNum in xrange(2,9):
    # for line in open('../data/'+str(date)+'_all', 'r'):
    for line in open('../data/small_data.txt', 'r'):
      featureArray = line.split("\t")
      if featureArray[10] == "":
        continue
      gender = featureArray[1]
      birthYear = featureArray[2]
      query = featureArray[7].replace('　', ' ')
      searchTime = featureArray[5].split(",")[0]
      device = featureArray[8]
      vertical = cm.typical_vertical(featureArray[10])
      length = len(query.split(" "))
      if length > 5:
        length = 5

      dic["all"]["all"] += 1
      dic[str(length)][vertical] += 1
      dic[str(length)]["all"] += 1


  cm.print_dict_content(dic)



