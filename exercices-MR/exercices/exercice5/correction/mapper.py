import sys
import csv
import re


def nettoyage(input: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\s]', '', input)


reader = csv.reader(sys.stdin)
next(reader)

for line in reader:
    names = nettoyage(line[1])
    streams = line[8]
    
    separated_names = names.split(',')
    
    for name in separated_names:
        print("%s\t%s" % (name.strip(), streams))