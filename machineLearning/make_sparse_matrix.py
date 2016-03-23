# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
from datetime import datetime
import common_method as cm
import array_method as am
import MeCab
import math
import numpy as np
from six.moves import cPickle
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
    for line in open('/home/c-yukadotami/data/small_data.txt', 'r'):
    # for line in open('/home/c-yukadotami/data/2015110'+str(fileNum)+'_all', 'r'):
      featureArray = line.split("\t")
      vertical = cm.typical_vertical(featureArray[10])
      if featureArray[10] == "":
        continue
      dic = {
        "array" : np.zeros(44),
        "answer": vertical
      }
      device = featureArray[8]
      birthYear = featureArray[2]
      gender = featureArray[1]
      if gender == '' or birthYear == '':
        continue
      query = featureArray[7]
      queris = query.replace('　', ' ').split(" ")
      term_len = len(queris)
      searchTime = featureArray[5].split(",")[0]
      date = cm.unix2date(float(searchTime))
      hour = cm.unix2hour(float(searchTime))
      is_holiday = cm.is_holiday(datetime.strptime(date,"%Y%m%d"))

      dic["array"] = am.s_device(dic["array"], device)
      dic["array"] = am.s_generation(dic["array"], birthYear)
      dic["array"] = am.s_gender(dic["array"], gender)
      dic["array"] = am.s_time(dic["array"], hour)
      if is_holiday:
        dic["array"][35] = 1
      dic["array"] = am.s_term_len(dic["array"], term_len)
      dic["array"] = am.s_speech(dic["array"], query)

      array.append(dic)

  with open("/home/c-yukadotami/pkl_data/array.pkl", 'wb') as f:
    cPickle.dump(array, f, protocol=cPickle.HIGHEST_PROTOCOL)





