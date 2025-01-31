import sys
import logging

logging.basicConfig(level=logging.INFO, filename="reducer.log", filemode="w")

current_year = None
current_playlist = 0
current_count = 0
index = 0

logging.info("Reducer started")

for index, line in enumerate(sys.stdin):
    year, playlist = line.split("\t")
    
    try:
        playlist = int(playlist)
    except:
        logging.info(f"Error in line <{index}: '{line}'>")
        continue
    
    if current_year == year:
        current_playlist += playlist
        current_count += 1
    else:
        if current_year:
            print("%s\t%.2f" % (current_year, current_playlist/current_count))
        current_year = year
        current_playlist = playlist
        current_count = 1

if current_year:    
    print("%s\t%.2f" % (current_year, current_playlist/current_count))

logging.info(f"line processed: {index}")
logging.info("Reducer finished")