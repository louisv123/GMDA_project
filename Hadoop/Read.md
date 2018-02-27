## COMPUTING RMSD WITH HADOOP

Transform the input file `aladip_implicit.txt` with `add_key.py`. This script adds a key for each conformation.

Then add the text file with the key (here for example `aladip_implicit_nbr.txt`) to hdfs with `hdfs dfs -put`

Launch the firt job : 
`hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -mapper "python /home/louis/Documents/Data_science/GMDA/job1_mapper.py" -reducer "python /home/louis/Documents/Data_science/GMDA/job1_reducer.py" -input "veillon_l/aladip_implicit_nbr.txt" -output "veillon_l/output"`

This first job take one atom as input `key x y z` and provide one conformation as output: `key [x1 y1 z1],[x2 y2 z2],...,[x10 y10 z10]`

As the reducing script sorts the output, we have to shuffle the output if we want to select only `m` of them.
Use the script `shuffling.py` to shuffle it. You can choose the number of conformation you want to keep by changing `m` in the script.

Here we have chosen `m = 100 000` conformation and the time cost is 2 hours for the next job. For `m = 200 000` conformation, the time cost is 8 hours.

then we compute the second job:

`hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -mapper "python /home/louis/Documents/Data_science/GMDA/job2_mapper.py" -reducer "python /home/louis/Documents/Data_science/GMDA/job2_reducer.py" -input "veillon_l/output/part-00000" -output "veillon_l/output1"`

In `job2_mapper.py`, you can changing `k` which is the number of nearest distance you keep in the output.

This second job takes as input `key [x1 y1 z1],[x2 y2 z2],...,[x10 y10 z10]` and provides as output `key 1 { key 2 : rmsd(confo 1, conf 2), key 18 : rmsd(confo 1, confo 18), ... , key 1586, rmsd(confo 1, confo 1589)}` with `k` nearest distance.
