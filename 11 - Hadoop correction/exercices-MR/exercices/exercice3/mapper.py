import sys
import csv

reader = csv.reader(sys.stdin)
next(reader) # enlever le header

for line in reader:
    released_year = line[3]
    streams = line[8]
    
    print("%s\t%s" % (released_year, streams))