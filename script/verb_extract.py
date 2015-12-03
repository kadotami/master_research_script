# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import MeCab

if __name__ == "__main__":
  for fileNum in xrange(2,9):
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
      featureArray = line.split("\t")
      query = featureArray[7]
      