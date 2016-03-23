# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
import datetime
import common_method as cm
import MeCab
import math
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

##
# [0] = sp, [1] = tab, [2] = pc
# [3)0's, [4] = 20's, [5] = 30's, [6]= 40's, [7] = 50's, [8] 60's
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

def s_term_len(array, len):
  if len ==1:
    array[36] = 1
  elif len ==2:
    array[37] = 1
  elif len ==3:
    array[38] = 1
  elif len ==4:
    array[39] = 1
  elif len >=5:
    array[40] = 1
  return array

def term_len(array, len):
  if len ==1:
    array = np.append(array,36)
  elif len ==2:
    array = np.append(array,37)
  elif len ==3:
    array = np.append(array,38)
  elif len ==4:
    array = np.append(array,39)
  elif len >=5:
    array = np.append(array,40)
  return array

def s_speech(array, query):
  try:
    query = unicode(query, 'utf-8')
  except:
    return array
  tagger = MeCab.Tagger("-Ochasen")
  encoded_text = query.encode('utf-8')
  node = tagger.parseToNode(encoded_text)
  verbFlag = False
  adjFlag = False
  joshiFlag = False
  while node:
    feature = node.feature
    speech = feature.split(",")[0]
    if speech in [r'動詞']:
      verbFlag = True
    if speech in [r'形容詞']:
      adjFlag = True
    if speech in [r'助詞']:
      joshiFlag = True
    node = node.next
  if verbFlag:
    array[41] = 1
  if adjFlag:
    array[42] = 1
  if joshiFlag:
    array[43] = 1
  return array

def speech(array, query):
  try:
    query = unicode(query, 'utf-8')
  except:
    return array
  tagger = MeCab.Tagger("-Ochasen")
  encoded_text = query.encode('utf-8')
  node = tagger.parseToNode(encoded_text)
  verbFlag = False
  adjFlag = False
  joshiFlag = False
  while node:
    feature = node.feature
    speech = feature.split(",")[0]
    if speech in [r'動詞']:
      verbFlag = True
    if speech in [r'形容詞']:
      adjFlag = True
    if speech in [r'助詞']:
      joshiFlag = True
    node = node.next
  if verbFlag:
    array = np.append(array,41)
  if adjFlag:
    array = np.append(array,42)
  if joshiFlag:
    array = np.append(array,43)
  return array

def s_generation(array, birthYear):
  today = datetime.datetime.today()
  if birthYear == '':
    return array
  generation = (today.year - int(birthYear)) // 10
  if generation <= 1:
    array[3] = 1
  elif generation == 2:
    array[4] = 1
  elif generation == 3:
    array[5] = 1
  elif generation == 4:
    array[6] = 1
  elif generation == 5:
    array[7] = 1
  elif generation >= 6:
    array[8] = 1
  return array

def generation(array, birthYear):
  today = datetime.datetime.today()
  if birthYear == '':
    return array
  generation = (today.year - int(birthYear)) // 10
  if generation <= 1:
    array = np.append(array,3)
  elif generation == 2:
    array = np.append(array,4)
  elif generation == 3:
    array = np.append(array,5)
  elif generation == 4:
    array = np.append(array,6)
  elif generation == 5:
    array = np.append(array,7)
  elif generation >= 6:
    array = np.append(array,8)
  return array

def s_device(array, device):
  if device == 'smartphone':
    array[0] = 1
  elif device == 'tablet':
    array[1] = 1
  elif device == 'pc':
    array[2] = 1
  return array

def device(array, device):
  if device == 'smartphone':
    array = np.append(array,0)
  elif device == 'tablet':
    array = np.append(array,1)
  elif device == 'pc':
    array = np.append(array,2)
  return array

def s_gender(array, gender):
  if gender == 'm':
    array[9] = 1
  elif gender == 'f':
    array[10] = 1
  return array

def gender(array, gender):
  if gender == 'm':
    array = np.append(array,9)
  elif gender == 'f':
    array = np.append(array,10)
  return array

def s_time(array, time):
  array[int(time)+11] = 1
  return array

def time(array, time):
  array = np.append(array,int(time)+11)
  return array
