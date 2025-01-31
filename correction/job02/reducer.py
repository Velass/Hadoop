import sys

current_magasin = None
current_cout = 0

for line in sys.stdin:
    magasin, cout = line.split("\t")
    
    try:
        cout = float(cout)
    except:
        continue # passe à la prochaine itération
    
    if current_magasin == magasin:
        current_cout += cout
    else:
        if current_magasin: # protection anti-None (1er ligne)
            print("%s\t%.2f" % (current_magasin, current_cout))
        current_magasin = magasin
        current_cout = cout
        
if current_magasin: # protection afficher le dernier élément
    print("%s\t%.2f" % (current_magasin, current_cout))