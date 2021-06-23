#! /usr/bin/python3
# Mapper.py

from math import sqrt, floor
import csv
import pandas as pd
import os
import sys
import numpy as np
from sklearn import preprocessing

def mapper(num):
  cent_dict = {}
  for line in sys.stdin: 
      point = [float(i) for i in line.split(',')]
      priority = np.random.uniform()
      if len(cent_dict) < num :
         cent_dict[priority] = point
      else :
         min_key = min(cent_dict.keys())
         if priority > min_key :
            del cent_dict[min_key]
            cent_dict[priority] = point
  for key in cent_dict:
     print(key,cent_dict[key],num)

if __name__ == "__main__":
  num_clusters=3
  mapper(num_clusters)

