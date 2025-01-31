import sys

for line in sys.stdin:
    parts = line.split("\t")
    
    magasin = parts[2]
    cout = parts[4]
    
    print("%s\t%s" % (magasin, cout))