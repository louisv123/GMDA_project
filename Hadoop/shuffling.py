import random
import numpy as np

data='/home/louis/Documents/Data_science/GMDA/part-00000' 

i = 100000 # number of conformation we keep

with open(data, 'r') as f:
    file_lines = [''.join([x]) for x in f.readlines()]
file_lines=random.sample(file_lines, i)

with open("part_2D", 'w') as f:
    f.writelines(file_lines) 




