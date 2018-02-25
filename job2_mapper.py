#!/usr/bin/env python
#job 2

#mapper_1
import os
import sys
import rmsd

store=[]

for line in sys.stdin:
	
	store.append(line)
	
	
for line in store:
	
	key_value1 = line.split(',')

	confo1=[]
	
	for j in range(10):
		atom=[]
		for i in range(3):
			atom.append(float(key_value1[j+1][3+i*7:9+i*7]))
		confo1.append(atom)
	


	
	for line_ in store:

	
		
		key_value2 = line_.split(',')
		
		confo2=[]
		
		for j in range(10):
			atom=[]
			for i in range(3):

				try:

					atom.append(float(key_value2[j+1][3+i*7:9+i*7]))
				except: 
					print(j+1)

			confo2.append(atom)

		try:
			
			value=rmsd.kabsch_rmsd(confo1,confo2)
		except:
			print('error rmsd')

			
		print '{},{}'.format([key_value1[0],key_value2[0]],value)
		