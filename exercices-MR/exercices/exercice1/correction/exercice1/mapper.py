import sys
import csv

for line in csv.DictReader(sys.stdin):
    released_year = line["released_year"]
    streams = line["streams"]
    
    print("%s\t%s" % (released_year, streams))