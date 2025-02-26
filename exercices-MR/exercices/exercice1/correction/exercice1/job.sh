#!/bin/bash

# Définition des variables d'entrée et de sortie
INPUT_FILE="Spotify_Most_Streamed_Songs.csv"
OUTPUT_FILE="exercice1"

# Copie du fichier d'entrée dans le HDFS
hdfs dfs -put $INPUT_FILE input

# Suppression du répertoire de sortie s'il existe déjà
hdfs dfs -rm -r output/$OUTPUT_FILE

# Lancement du job Hadoop avec les scripts mapper et reducer
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -file mapper.py -mapper "python3 mapper.py" -file reducer.py -reducer "python3 reducer.py" -input input/$INPUT_FILE -output output/$OUTPUT_FILE