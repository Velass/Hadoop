import sys

# Parcourez les lignes du CSV
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    # Extraire les champs du CSV
    track_name = line[0]
    artists_name = line[1]
    artist_count = line[2]
    
    # Afficher les champs
    print("%s;%s;%s" % (track_name, artists_name, artist_count))