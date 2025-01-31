import sys

current_magasin = None
current_cout = 0
current_count = 0

for line in sys.stdin:
    magasin, cout = line.split("\t")
    
    try:
        cout = float(cout)
    except ValueError:
        continue
    
    if current_magasin == magasin:
        current_cout += float(cout)
        current_count += 1
    else:
        if current_magasin:
            print('%s\t%.2f\t%.2f' % (current_magasin, current_cout, current_cout/current_count))
        current_magasin = magasin
        current_cout = cout
        current_count = 1

if current_magasin:
    print('%s\t%.2f\t%.2f' % (current_magasin, current_cout, current_cout/current_count))