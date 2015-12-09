# -*- coding: utf-8 -*-

## 動詞が含まれる場合のvertical
from collections import defaultdict
import datetime
import MeCab

## verticalを大きなまとめに
def typical_vertical(vertical):
  if vertical in ["isrch", "isearch", "bigimage"]:
    return "image"
  elif vertical in ["vsrch", "vsearch", "gvideo", "movie", "mvrnk", "drama", "tv", "tvrank"]:
    return "video"
  elif vertical in ["dic", "kb", "wiki"]:
    return "dic"
  elif vertical in ["chie"]:
    return "chie"
  elif vertical in ["map", "maps", "tv-spot"]:
    return "map"
  elif vertical in ["realtime", "rts", "buzz"]:
    return "realtime"
  elif vertical in ["news"]:
    return "news"
  elif vertical in ["shp", "cmcnb", "shpkw", "shprank", "cmcat", "fashion", "dcomic", "store", "adcomic"]:
    return "shopping"
  elif vertical in ["auc", "auction"]:
    return "auction"
  elif vertical in ["talent", "tlnt", "psnsp", "avtlnt"]:
    return "talent"
  elif vertical in ["recipe", "rcp", "cookpad", "hrecipe"]:
    return "recipe"
  elif vertical in ["loco", "local", "iplocal"]:
    return "loco"
  else:
    return "other"

## dicの中身をソートして出力
def print_dict_content(dic):
  for v in dic:
    allNum = dic["all"]
    if allNum == 0:
      continue
    print ("----------"+v+"----------")
    dic = sorted(dic.items(), key=lambda x: x[1])
    for y in dic:
      print (y[0]+','+str(y[1]) + "," + str(float(y[1])/allNum * 100) + "%")

if __name__ == "__main__":
  verbDic = defaultdict(lambda: 0)
  for fileNum in xrange(2,9):
    # for line in open('../data/2015110'+str(fileNum)+'_all', 'r'):
    for line in open('../data/small_data.txt','r'):
      featureArray = line.split("\t")
      if featureArray[11] != "":
        if featureArray[10] == "":
          continue
        vertical = typical_vertical(featureArray[10])
        query = featureArray[7]
        tagger = MeCab.Tagger("-Ochasen")
        encoded_text = query.encode('utf-8')
        node = tagger.parseToNode(encoded_text)
        verbFlag = False
        while node:
          feature = node.feature
          source = feature.split(",")[6]
          speech = feature.split(",")[0]
          word_kind = feature.split(",")[1]
          if speech in [r'動詞']:
            verbFlag = True
        if verbFlag:
          verbDic["all"] += 1
          verbDic[vertical] += 1


  print_dict_content(verbDic)


