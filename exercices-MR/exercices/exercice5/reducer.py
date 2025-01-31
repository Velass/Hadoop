import sys
import happybase
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#hbase

# connection = happybase.Connection('127.0.0.1', 9090)
connection = happybase.Connection('node188564-env-1839015-2024-d10-etudiant06.sh1.hidora.com', 12125)
connection.open()
if b'spotify' not in connection.tables():
    connection.create_table('spotify', {'artist': dict(), 'stream': dict()})
spotify = connection.table('spotify')

try:
    connection.disable_table(spotify)
    connection.delete_table(spotify)
except Exception:
    pass

#données

data = []
current_artist = None
current_stream = 0


for line in sys.stdin:
    if "\t" not in line:
        continue
    artist, stream = line.split("\t")
    
    try:
        artist = str(artist)
        stream = int(stream)
    except:
        continue
    
    if current_artist == artist:
        current_stream += stream
    else:
        if current_artist:
            data.append((current_artist, current_stream))
        current_artist = artist
        current_stream = stream
        spotify.put((current_artist.encode()), {'artist:name'.encode(): current_artist.encode(), 'stream:count'.encode(): str(current_stream).encode()})

if current_artist:    
    data.append((current_artist, current_stream))
    spotify.put((current_artist.encode()), {'artist:name'.encode(): current_artist.encode(), 'stream:count'.encode(): str(current_stream).encode()})
    

for key, value in spotify.scan():
     print(key, value)




df = pd.DataFrame(data, columns=["Artist", "Streams"])

# trier par rapport au streams décroissant
# tableau_triee = sorted(data, key=lambda x: x[1], reverse=True)
df = df.sort_values(by="Streams", ascending=False)

# afficher sur les 10 premiers
top_10 = df.head(10)

plt.figure()
plt.pie(top_10["Streams"], labels=top_10["Artist"], autopct="%1.1f%%", startangle=140)
plt.title("Top 10 des artistes les plus écoutés")
plt.tight_layout()
plt.xlabel("Nombre de streams")
plt.ylabel("Artiste")

with PdfPages('resultat.pdf') as pdf:
    pdf.savefig()  # Sauvegarder le graphe dans le fichier PDF

plt.show()
connection.close()