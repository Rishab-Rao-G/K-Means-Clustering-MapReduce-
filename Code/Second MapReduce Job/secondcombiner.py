#!/usr/bin/python3
#Combiner.py
from math import sqrt, floor
import os
import sys
import re
import numpy as np
from collections import defaultdict

points_sum = np.array([])
rowcount = 0
initial_key = -1
data_row = []
current_key = -1
for line in sys.stdin:
  data_list = []
  r = [i for i in line.split(' ')]
  for i in r:
    x = re.sub("\[|\]|,","",i)
    x = x.replace('\n','')
    x = float(x)
    data_list.append(x)
  data_row.append(data_list)

for point in data_row:
  key = int(point[0])
  current_key = key
  value = point[1:-1]
  if current_key == initial_key:
    points_sum += value
    rowcount += 1
  else:
    if rowcount != 0:
      print(initial_key,list(points_sum),rowcount)

    initial_key = current_key
    points_sum = np.array(value)
    rowcount = 1
if current_key == initial_key and rowcount != 0:
  print(current_key,list(points_sum),rowcount)




