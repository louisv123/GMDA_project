## COMPUTING RMSD WITH HADOOP

Transform the input file `aladip_implicit.txt` with `add_key.py`. This script adds a key for each conformation.

Then add the input file `aladip_implicit_nbr.txt` to hdfs with `hdfs dfs -put`

Launch the firt job : 
`hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -mapper "python /home/louis/Documents/Data_science/GMDA/job1_mapper.py" -reducer "python /home/louis/Documents/Data_science/GMDA/job1_reducer.py" -input "veillon_l/aladip_implicit_nbr.txt" -output "veillon_l/output"`

then the second job:
`hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -mapper "python /home/louis/Documents/Data_science/GMDA/job2_mapper.py" -reducer "python /home/louis/Documents/Data_science/GMDA/job2_reducer.py" -input "veillon_l/output/part-00000" -output "veillon_l/output1"`
