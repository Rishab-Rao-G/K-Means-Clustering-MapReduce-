#!/usr/bin/python3
#Mapper phase 2

from math import sqrt, floor
import csv
import pandas as pd
import os
import sys
import numpy as np
from sklearn import preprocessing
from scipy.spatial import distance
import re


i_centroids = []
cent_f = open('initcent.txt','r')
for cent in cent_f:
  cf = [i for i in cent.split(',')]
  cf.pop()
  centlist = []
  for i in cf:
    x = re.sub("\[|\]|,","",i)
    x = x.replace('\n','')
    x = float(x)
    centlist.append(x)
  i_centroids.append(centlist)

for line in sys.stdin:
  data = [float(i) for i in line.split(',')]
  distances = [distance.euclidean(data,center) for center in i_centroids]
  min_dist = min(distances)
  print(distances.index(min_dist),data,1)





