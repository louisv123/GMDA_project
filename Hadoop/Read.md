## COMPUTING RMSD WITH HADOOP

This script uses hadoop distributed file system

### INPUT FILE OF JOB 1.

Transform the input file `aladip_implicit.txt` with `add_key.py`. This script adds a key for each conformation.

Then add the text file with the key (here for example `aladip_implicit_nbr.txt`) to hdfs with `hdfs dfs -put`

### RUNNING JOB 1.

Launch the firt job : 
`hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -mapper "python /home/louis/Documents/Data_science/GMDA/job1_mapper.py" -reducer "python /home/louis/Documents/Data_science/GMDA/job1_reducer.py" -input "veillon_l/aladip_implicit_nbr.txt" -output "veillon_l/output"`

This first job take one atom as input `key x y z` and provide one conformation as output: `key [x1 y1 z1],[x2 y2 z2],...,[x10 y10 z10]`

### INPUT FILE JOB 2.

As the reducing script sorts the output, we have to shuffle the output.
Use the script `shuffling.py` .


### RUNNING JOB 2.

then we compute the second job:

`hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -mapper "python /home/louis/Documents/Data_science/GMDA/job2_mapper.py 15000 100000 matrix" -reducer "python /home/louis/Documents/Data_science/GMDA/job2_reducer.py" -input "veillon_l/output/part-00000" -output "veillon_l/output1"`

In `job2_mapper.py`, you can changing `k` which is the number of distance you keep in the output, `m` the number of sample in the input file of job 2 and the format of the output of job 2 `matrix` or `dictionnary`.

Example:
```job2_mapper.py 15000 100000 matrix```

This second job takes as input `key [x1 y1 z1],[x2 y2 z2],...,[x10 y10 z10]` and provides as output either:

```key 1 { key 2 : rmsd(confo 1, conf 2), key 18 : rmsd(confo 1, confo 18), ... , key 1586, rmsd(confo 1, confo 1589)}``` 

or 

```[[key 1, rmsd(confo 1, conf 2) rmsd(confo 1, confo 18) ...  rmsd(confo 1, confo 1589)],...,[key 50, rmsd(confo 50, conf 2) rmsd(confo 50, confo 18) ...  rmsd(confo 50, confo 1589)]]````




