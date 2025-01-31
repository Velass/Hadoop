import sys

for line in sys.stdin: 
    line = line.strip() 
    for word in line.split("\t"): 
        if len(word) > 0 : 
            print("%s\t%i" %(word.lower(), 1)) 