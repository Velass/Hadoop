import sys

current_year = None
current_streams = 0

for line in sys.stdin:
    year, streams = line.split("\t")
    
    try:
        streams = int(streams)
    except:
        continue
    
    if current_year == year:
        current_streams += streams
    else:
        if current_year:
            print("%s\t%s" % (current_year, current_streams))
        current_year = year
        current_streams = streams

if current_year:    
    print("%s\t%s" % (current_year, current_streams))