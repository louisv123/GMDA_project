import sys
sys.path.insert(0, '/home/louis/Documents/Data_science/GMDA/ToMATo_code/ToMATo/IRMSD-master/python/IRMSD')
from math import sqrt
import unittest

import numpy as np

from IRMSD import Conformations
from IRMSD import align_array
import IRMSD
import time
data='/home/louis/Documents/Data_science/GMDA/aladip_implicit.txt' #aladip_implicit

data_frame=np.loadtxt(data)
dim=3 #nbr of dimension
n=10 #nbr of atom for one conformation
k=3 #nbr of distance we keep 
structure=data_frame.reshape((data_frame.shape[0]/n,dim,n))

RMSD={}
confs = align_array(structure, 'axis')
conf_obj = Conformations(confs, 'axis', 10)

for i in range(1000): #data_frame.shape[0]/n
	rmsd_dic={}
	rmsds = conf_obj.rmsds_to_reference(conf_obj,i)
	rmsds_sorted=sorted(rmsds)
	for l in range(k):
		rmsd_dic[l]=rmsds_sorted[l]
	RMSD[i]=rmsd_dic
	







