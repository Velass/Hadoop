import sys

current_magasin = None
current_cout= 0


for line in sys.stdin:
    parts = line.split("\t")
    magasin = parts[0]
    cout = parts[1]
    current_count = 0
    
    
    try:
        cout = float(current_cout)
    except:
        continue
    
    if current_magasin == magasin:
        current_cout += cout
    else:
        if current_magasin:
            print("%s\t%.2f\%f" % (current_magasin, current_cout))
        current_magasin = magasin
        current_cout = cout
        current_count = 1
    
if current_magasin:
    print("%s\t%.2f" % (current_magasin,current_cout))
    