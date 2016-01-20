# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import re

#
# クックパッドかレシピがクエリに含まれている場合の
# レシピ、クックパッドヴァーティカルの割合を調べる
#

def print_dict_content(dic):
  allNum = dic["all"]
  dic = sorted(dic.items(), key=lambda x: x[1])
  for x in dic:
    print (x[0]+','+str(x[1]) + "," + str(float(x[1])/allNum * 100) + "%")


if __name__ == "__main__":
  verticals = defaultdict(lambda: 0)
  querys = []
  rexp = [re.compile(r'.*%s.*' % "クックパッド"), re.compile(r'.*%s.*' % "レシピ")]
  for fileNum in xrange(2,9):
    # for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
    for line in open('../data/small_data.txt', 'r'):
      featureArray = line.split("\t")
      vertical = featureArray[10]
      gender = featureArray[1]
      if vertical == "":
        continue
      for pattern in rexp:
        if pattern.match(featureArray[7]):
          if vertical in ["recipe", "cookpad", "hrecipe", "rcp"]:
            verticals["recipe"] += 1
            verticals["all"] += 1
          else:
            verticals[vertical] += 1
            verticals["all"] += 1
  print_dict_content(verticals)