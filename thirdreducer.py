#! /usr/bin/python

from math import sqrt, floor
import os
import sys
import re
from collections import defaultdict


cluster = defaultdict(list)
data_row = []
for line in sys.stdin:
  print(line)
