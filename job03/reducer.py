import sys

current_magasin = None
current_cout = 0
current_count = 0

for line in sys.stdin:
    magasin, cout = line.split("\t")
    
    try:
        cout = float(cout)
    except:
        continue # passe à la prochaine itération
    
    if current_magasin == magasin:
        current_cout += cout
        current_count += 1 # current_count++ // ++current_count
    else:
        if current_magasin: # protection anti-None (1er ligne)
            moyenne = current_cout/current_count
            print("%s\t%.2f\t%f" % (current_magasin, current_cout, moyenne))
        current_magasin = magasin
        current_cout = cout
        current_count = 1
        
if current_magasin: # protection afficher le dernier élément
    print("%s\t%.2f\t%f" % (current_magasin, current_cout, current_cout/current_count))