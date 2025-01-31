import sys
import csv
import logging

logging.basicConfig(level=logging.DEBUG, filename='mapper.log', filemode='w')

reader = csv.reader(sys.stdin)
next(reader)

logging.info("Mapper started")

for index, line in enumerate(reader):
    released_year = line[3]
    in_spotify_playlists = line[6]
    
    print("%s\t%s" % (released_year, in_spotify_playlists))

logging.info(f"line processed: {index}")
logging.info("Mapper finished")