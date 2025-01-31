##########
# IMPORT #
##########

import sys
import happybase

#############
# HAPPYBASE #
#############

# Configurer la connexion à HBase
IP = 'node188358-env-1839015-hadoop-robin.sh1.hidora.com'
PORT = 11705 # Port public couplé au port privé 9090 de HBase
connection = happybase.Connection(IP, PORT) 
connection.open()

# Nom de la table HBase
hbase_table_name = 'streams_songs'

# Supprimer la table HBase si elle existe déjà
try:
    connection.disable_table(hbase_table_name)
    connection.delete_table(hbase_table_name)
except Exception:
    pass

# Créer une table HBase avec des column families
column_families = {
    'info': dict(),
    'stat': dict()
}
connection.create_table(hbase_table_name, column_families)
table = connection.table(hbase_table_name)

#############
# AGGREGATE #
#############

current_artist = None
current_stream = 0

# Boucler sur les données
for index, line in enumerate(sys.stdin):
    artist_name, streams = line.split(';')
    
    # Protection anti-crash: conversion 'streams' en entier
    try:
        streams = int(streams)
    except ValueError:
        continue
    
    # aggrégation des données
    if current_artist == artist_name:
        current_stream += streams
    else:
        # Insertion si l'artiste n'est pas 'None'
        if current_artist:
            # Extraire et convertir les champs en bytes
            index = str(index).encode()
            data = {
                b'stat:artist_name': current_artist.encode(),
                b'info:artist_count': str(current_stream).encode()
            }
            
            # Insérer les données dans HBase
            table.put(index, data)
        
        # Réinitialiser les variables
        current_artist = artist_name
        current_stream = streams

# Insérer la dernière ligne
if current_artist:
    index = str(index).encode()
    data = {
        b'stat:artist_name': current_artist.encode(),
        b'info:artist_count': str(current_stream).encode()
    }
    table.put(index, data)
    
# Fermer la connexion
connection.close()