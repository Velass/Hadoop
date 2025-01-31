#!/usr/bin/env python3
import sys

current_year = None
total_streams = 0

for line in sys.stdin:
    try:
        year, stream = line.strip().split(";")  # Séparer les valeurs
        stream = int(stream)  # Convertir les streams en entier

        if current_year and current_year != year:
            print("%s\t%s" % (current_year, total_streams))
            total_streams = 0

        current_year = year
        total_streams += stream

    except :
        continue
    
# Dernière ligne
if current_year:
    print("%s\t%s" % (current_year, total_streams))
