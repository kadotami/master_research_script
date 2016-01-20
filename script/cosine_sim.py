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
import scipy.spatial.distance as dis
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
  array = numpy.load("array.npy")
  vocab = numpy.load("vocab.npy")
  while 1:
    word = raw_input("単語を入力してください")
    try:
      index = numpy.where(vocab == word)[0]
      img_index = numpy.where(vocab == "image")[0]
      vdo_index = numpy.where(vocab == "video")[0]
      rcp_index = numpy.where(vocab == "recipe")[0]
      news_index = numpy.where(vocab == "news")[0]
      dic_index = numpy.where(vocab == "dic")[0]
      shp_index = numpy.where(vocab == "shopping")[0]
      auc_index = numpy.where(vocab == "auction")[0]
      chie_index = numpy.where(vocab == "chie")[0]
      real_index = numpy.where(vocab == "realtime")[0]
      talent_index = numpy.where(vocab == "talent")[0]
      map_index = numpy.where(vocab == "map")[0]
      loco_index = numpy.where(vocab == "loco")[0]
      print "img", 1-dis.cosine(array[index], array[img_index])
      print "video", 1-dis.cosine(array[index], array[vdo_index])
      print "recipe", 1-dis.cosine(array[index], array[rcp_index])
      print "news", 1-dis.cosine(array[index], array[news_index])
      print "dic", 1-dis.cosine(array[index], array[dic_index])
      print "shp", 1-dis.cosine(array[index], array[shp_index])
      print "auc", 1-dis.cosine(array[index], array[auc_index])
      print "chie", 1-dis.cosine(array[index], array[chie_index])
      print "real", 1-dis.cosine(array[index], array[real_index])
      print "talent", 1-dis.cosine(array[index], array[talent_index])
      print "map", 1-dis.cosine(array[index], array[map_index])
      print "loco", 1-dis.cosine(array[index], array[loco_index])
    except:
      print "登録されていません"



