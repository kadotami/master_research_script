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
#   特定の単語数のクエリを抽出
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
      query = featureArray[7].replace('　', ' ')
      vertical = cm.typical_vertical(featureArray[10])
      if vertical != "video":
        continue
      length = len(query.split(" "))
      if length > 4:
        print featureArray[7]