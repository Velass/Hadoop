OUTPUT_DIR = 'job01'
INPUT_FILE = 'purchases.txt'

hdfs dfs -rm -r output/$OUTPUT_DIR

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -file mapper.py -mapper "python3 mapper.py" -file reducer.py -reducer "python3 reducer.py" -input input/$INPUT_FILE -output output/$OUTPUT_DIR

hdfs dfs -cat output/$OUTPUT_DIR/part-00000