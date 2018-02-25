#!/usr/bin/env python
#job 1

#mapper_1
import os
import sys

value=[0,0]
for line in sys.stdin:
	value[0] = line.split(' ')[0]
	value[1] = line[line.find(' '):-1]
	print '{},{},{}'.format(value[0],value[1], "ee" )


#os.environ['mapreduce_map_input_file']
