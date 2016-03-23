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
from sklearn.svm import LinearSVC

if __name__ == '__main__':
  array = cPickle.load('/home/c-yukadotami/pkl_data/array.pkl')
  data_training = [x["array"] for x in array]
  label_training = [int(cm.label2id(x["answer"])) for x in array]

  estimator = LinearSVC(C=1.0)
  estimator.fit(data_training, label_training)

  label_prediction = estimator.predict(data_test)

  print(label_prediction)