# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
from datetime import datetime
import common_method as cm
import MeCab
import math
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

##
# [0] = sp, [1] = tab, [2] = pc
# [3] = 10's, [4] = 20's, [5] = 30's, [6]= 40's, [7] = 50's, [8] 60's
# [9] = male, [10] = female
# [11] ~ [34] = time
# [35] is holiday
# [36] term_len == 1
# [37] term_len == 2
# [38] term_len == 3
# [39] term_len == 4
# [40] term_len == 5以上
# [41] = verb
# [42] = adj
# [43] = joshi
#

if __name__ == '__main__':
  array = []

  for fileNum in xrange(2,9):
    date = '2015110'+str(fileNum)
    for line in open('../data/'+str(date)+'_all', 'r'):
      featureArray = line.split("\t")
      vertical = cm.typical_vertical(featureArray[10])
      if vertical == "":
        continue
      dic = {
        "array" : np.zeros(43),
        "answer": vertical
      }
      device = featureArray[8]
      birthYear = featureArray[2]
      gender = featureArray[1]
      query = featureArray[7]
      queris = query.replace('　', ' ').split(" ")
      searchTime = featureArray[5].split(",")[0]
      
      hour = cm.unix2hour(float(searchTime))
      is_holiday = cm.is_holiday(datetime.strptime(date,"%Y%m%d"))

# 品詞
      try:
        query = unicode(query, 'utf-8')
      except:
        continue
      tagger = MeCab.Tagger("-Ochasen")
      encoded_text = query.encode('utf-8')
      node = tagger.parseToNode(encoded_text)
      verbFlag = False
      adjFlag = False
      joshiFlag = False
      while node:
        speech = feature.split(",")[0]
        if speech in [r'動詞']:
          verbFlag = True
        if speech in [r'形容詞']:
          adjFlag = True
        if speech in [r'助詞']:
          joshiFlag = True
        node = node.next
      if verbFlag:
        dic.array[41] = 1
      if adjFlag:
        dic.array[42] = 1
      if joshiFlag:
        dic.array[43] = 1



