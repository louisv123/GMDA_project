import sys
sys.path.insert(0, '/home/louis/Documents/Data_science/GMDA/ToMATo_code/ToMATo/IRMSD-master/python/IRMSD')
from math import sqrt
import unittest

import numpy as np

from IRMSD import Conformations
from IRMSD import align_array
import IRMSD

data='/home/louis/Documents/Data_science/GMDA/test.xyz'

with open(data) as f:
	for l in f:
		x, y, z = l.split()
		print(x)

