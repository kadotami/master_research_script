# -*- coding: utf-8 -*-
from collections import defaultdict
import datetime
import re


if __name__ == "__main__":
  rexps = []
  rexps.append(re.compile(r'.*%s.*' % "www\.youtube"))
  rexps.append(re.compile(r'.*%s.*' % "m\.youtube"))
  rexps.append(re.compile(r'.*%s.*' % "www\.nicovideo"))
  rexps.append(re.compile(r'.*%s.*' % "sp\.nicovideo"))
  all_num = 0
  video = 0
  for fileNum in xrange(2,9):
    for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
      featureArray = line.split("\t")
      url = featureArray[11]
      browseId = featureArray[0]
      device = featureArray[8]
      vertical = cm.typical_vertical(featureArray[10])
      birthYear = featureArray[2]
      gender = featureArray[1]
      all_num += 1
      for rexp in rexps:
        if rexp.match(url):
          video += 1

  print video
  print all_num

