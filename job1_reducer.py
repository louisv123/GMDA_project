#!/usr/bin/env python
#job 1

#reducer_1
import sys

node_link={}

for line in sys.stdin:

	#from (node1, node2) we compute (node1,page_rank,node1_out1, node1_out2,...)

	#get the node 1 node 2 and the file name
	key, value, f_name=line.split(',')
	#get only the file name
	#f_name=f_name.split('/')[-1]

	if key in node_link.keys():
		node_link[key].append(value)
	else:
		node_link[key]=[value]

for key in node_link.keys():
	print '{},{}'.format(key,node_link[key])