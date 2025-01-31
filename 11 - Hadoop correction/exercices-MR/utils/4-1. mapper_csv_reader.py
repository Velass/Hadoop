import sys
import csv

# Créez un lecteur CSV pour gérer les données
csv_reader = csv.reader(sys.stdin)

# OPTIONNEL : Ignorer le header du CSV
next(csv_reader)

# Parcourez les lignes du CSV
for line in csv_reader:
    
    # Extraire les champs du CSV
    track_name = line[0]
    artists_name = line[1]
    artist_count = line[2]
    
    # Afficher les champs
    print("%s;%s;%s" % (track_name, artists_name, artist_count))