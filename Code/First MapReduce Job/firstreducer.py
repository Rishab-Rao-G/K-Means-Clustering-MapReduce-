#! /usr/bin/python3
import os,sys
import re

data = {}
for line in sys.stdin:
  line_list = []
  ip = [i for i in line.split(" ")]
  for i in ip:
    x = re.sub("\[|\]|,","", i)
    x = x.replace('\n','')
    x = float(x)
    line_list.append(x)
  priority = line_list[0]
  point = line_list[1:-1]
  k = int(line_list[-1])
  point.append("cent")
  if len(data) < k :
    data[priority] = point
  else :
    min_key = min(data.keys())
    if priority > min_key :
      del data[min_key]
      data[priority] = point
for key in data.keys():
  print(data[key])


