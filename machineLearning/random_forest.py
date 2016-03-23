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
from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':
  with open('/home/c-yukadotami/pkl_data/array.pkl', 'rb') as pickle_file:
    array = cPickle.load(pickle_file)
  data_training = np.array([])
  for x in xrange(1,300):
    np.append(data_training, array[x]["array"])
  label_training = np.array([])
  for x in xrange(1..300):
    np.append(label_training,int(cm.label2id(array[x]["answer"])))
  # for x in array:
  #   np.append(data_training, x["array"])
  # label_training = np.array([])
  # for x in array:
  #   np.append(label_training,int(cm.label2id(x["answer"])))
  print data_training
  print label_training
  estimator = RandomForestClassifier()
  estimator.fit(data_training, label_training)

  label_prediction = estimator.predict([1,35])

  for id in label_prediction:
    print(cm.id2label(id))
