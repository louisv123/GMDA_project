#!/usr/bin/env python
#job 2

#mapper_1

import os

import sys

# the path of IRMSD library
sys.path.insert(0, '/home/louis/Documents/Data_science/GMDA/ToMATo_code/ToMATo/IRMSD-master/python/IRMSD')

import unittest

import numpy as np

from IRMSD import Conformations
from IRMSD import align_array
import IRMSD

m=100000 #nbr of input conformation
dim=3 #space dimension
n=10 #nbr of atom for one conformation
k=15000 #nbr of distance we keep

#we create a one dimensional array with all data
conformation=[0]*m*dim*10

li=0
for line in sys.stdin:

	""" the input is (key, '[x1 y1 z1],[x2 y2 z2],...,[x10 y10 z10]')

	here we compute the rmsd distance between each pairwise conformation:
	output:

	([key 1, key 2], rmsd(confo_1, confo_2))
	"""
	
	# we get the input 
	key_value1 = line.split(',')

	
	for atom in range(n):
		
		for coord in range(dim):
			conformation[m*n*coord+m*atom+li]=float(key_value1[atom+1][3+coord*7:9+coord*7])
			#data.append(float(key_value1[atom+1][3+coord*7:9+coord*7]))
		
	li+=1
# we convert data into numpy array
conformation=np.array(conformation)
#we reshape the one dimensional array into 100000 x 3 x 10
conformation=conformation.reshape((len(conformation)/3/n,3,n))

# we create conformation array
confs = align_array(conformation, 'axis')
# we create conformation object
conf_obj = Conformations(confs, 'axis', 10)

#for each conformation
for i in range(conformation.shape[0]): #data_frame.shape[0]/n

	rmsd_dic={}
	# we compute the rmsd between conformation i and all other confomations
	rmsds = conf_obj.rmsds_to_reference(conf_obj,i)
	# we sort the conformation 
	rmsds_sorted=sorted(rmsds)

	#we keep only the k nearest conformation
	for l in range(k):
		rmsd_dic[l]=rmsds_sorted[l]

	# we print output
	print '{},{}'.format(i,rmsd_dic)
	

