# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import re

#
# 「画像」がクエリに含まれていた場合のvertical
#

## dicの中身をソートして出力
def print_dict_content(dic):
  for v in dic:
    allNum = dic[v]["all"]
    print ("----------"+v+"----------")
    dic[v] = sorted(dic[v].items(), key=lambda x: x[1])
    for y in dic[v]:
      print (y[0]+','+str(y[1]) + "," + str(float(y[1])/allNum * 100) + "%")

if __name__ == "__main__":
  result = {
    "「画像」あり": defaultdict(lambda: 0),
    "「画像」なし": defaultdict(lambda: 0)
  }
  rexp = re.compile(r'.*%s.*' % "画像")
  for fileNum in xrange(2,9):
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
      featureArray = line.split("\t")
      if featureArray[11] == "":
        continue
      if featureArray[10] in ["isearch", "bigimage"]:
        if rexp.match(featureArray[7]):
          result["「画像」あり"][featureArray[10]] += 1
          result["「画像」あり"]["all"] += 1
        else:
          result["「画像」なし"][featureArray[10]] += 1
          result["「画像」なし"]["all"] += 1
      elif featureArray[10] != "isrch":
        if rexp.match(featureArray[7]):
          result["「画像」あり"][featureArray[10]] += 1
          result["「画像」あり"]["all"] += 1

  print_dict_content(result)
