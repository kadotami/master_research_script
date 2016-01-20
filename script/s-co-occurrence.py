# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
from datetime import datetime
import common_method as cm
import MeCab
import numpy
import math
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import svds
reload(sys)
sys.setdefaultencoding('utf-8')

def query_array(query):
  array = []
  queries = query.replace("　"," ").split(" ")
  for q in queries:
    q_str = ""
    tagger = MeCab.Tagger("-Ochasen")
    encoded_text = q.encode('utf-8')
    node = tagger.parseToNode(encoded_text)
    while node:
      source = node.feature.split(",")[6]
      if source != "*":
        array.append(source)
        q_str = q_str + source
      node = node.next
    array.append(q_str)
  return array

def make_dic(dec, query_words):
  for qw in query_words:
    dic.setdefault(qw,{})
    for qw2 in query_words:
      dic[qw].setdefault(qw2,0)
      if qw != qw2:
        dic[qw][qw2] += 1
  return dic

def make_matrix(dic):
  keys = dic.keys()
  array = numpy.zeros(len(keys))
  vocab = numpy.array([])
  for k,v in dic.items():
    line = numpy.array([])
    vocab = numpy.append(vocab,k)
    for key in keys:
      if v.get(key) == None:
        line = numpy.append(line,0)
      else:
        line = numpy.append(line, v[key])
    array = numpy.vstack((array,line))
  array = numpy.delete(array,0,0)
  numpy.save('s_array', array)
  numpy.save('s_vocab', vocab)


if __name__ == '__main__':
  dic = {}
  for fileNum in xrange(2,9):
    date = '2015110'+str(fileNum)
    # for line in open('../data/'+date+'_all', 'r'):
    for line in open('../data/small_data.txt', 'r'):
      featureArray = line.split("\t")
      if featureArray[10] == "":
        continue
      try:
        query = unicode(featureArray[7], 'utf-8')
      except:
        continue
      is_holiday = cm.is_holiday(datetime.strptime(date,"%Y%m%d"))
      browseId = featureArray[0]
      device = featureArray[8]
      vertical = cm.typical_vertical(featureArray[10])
      birthYear = featureArray[2]
      gender = featureArray[1]
      query_words = query_array(query) # クエリを形態素で分割したものも入れる
      query_words.append(vertical.encode('utf-8'))
      dic = make_dic(dic, query_words)
    make_matrix(dic)
    array = numpy.load('s_array.npy')
    svd_array = svds(array,200)[0]
    for vec in svd_array:
      if numpy.linalg.norm(vec) != 0:
        vec /= numpy.linalg.norm(vec)
    numpy.save('s_array_200', svd_array)

