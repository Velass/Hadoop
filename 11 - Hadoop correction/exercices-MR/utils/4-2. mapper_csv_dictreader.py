import sys
import csv

# /!\ Considère que le fichier CSV possède un header.
# Sinon, il faut le rajouter manuellement.
csv_reader = csv.DictReader(sys.stdin)

# Parcourez les lignes du CSV
for line in csv_reader:
    
    # Extraire les champs du CSV
    track_name = line["track_name"]
    artists_name = line["artist(s)_name"]
    artist_count = line["artist_count"]
    
    # Afficher les champs
    print("%s;%s;%s" % (track_name, artists_name, artist_count))