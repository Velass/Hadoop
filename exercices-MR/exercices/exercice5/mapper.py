import sys
import csv
import re


def nettoyage(input: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\s]', '', input)

# Créez un lecteur CSV pour gérer les données
csv_reader = csv.reader(sys.stdin)

# OPTIONNEL : Ignorer le header du CSV
next(csv_reader)

# Parcourez les lignes du CSV
for line in csv_reader:
    
    # Extraire les champs du CSV
    artist = nettoyage(line[1])
    stream = line[8]
    # r'[^\x00-\x7F]+'
    separated_names = artist.split(',')
    
    # Afficher les champs
    for artist in separated_names:
        print("%s\t%s" % (artist.strip(), stream))
    
# todo modif de la , pour les chanteur soucis avec le sort