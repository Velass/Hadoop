import sys
import csv

# Créez un lecteur CSV pour gérer les données
csv_reader = csv.reader(sys.stdin)

# OPTIONNEL : Ignorer le header du CSV
next(csv_reader)

# Parcourez les lignes du CSV
for line in csv_reader:
    
    # Extraire les champs du CSV
    year = line[3]
    stream = line[8]
    
    # Afficher les champs
    print("%s\t%s" % (year, stream))