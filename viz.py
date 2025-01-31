import happybase
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# plt.style.use('classic')

# Configurer la connexion à HBase
IP = '127.0.0.1'
PORT = 9090
connection = happybase.Connection(IP, PORT)
connection.open()

# Nom de la table HBase
hbase_table_name = 'streams_songs'

table = connection.table(hbase_table_name)

aggregated = []

for key, data in table.scan():
    aggregated.append((data[b'stat:artist_name'].decode(), int(data[b'info:streams_count'].decode())))

df = pd.DataFrame(aggregated, columns=["Artist Name", "Streams"])

# Trier et sélectionner le top 100
top_100 = df.sort_values("Streams", ascending=False, inplace=False).head(100)

# Créer le graphique
plt.figure(figsize=(8.27, 11.69))  # Taille A4 en pouces (21 cm x 29,7 cm)
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.05, top=0.95)
bars = plt.barh(top_100["Artist Name"], top_100["Streams"], edgecolor="white", linewidth=0.7)
plt.gca().invert_yaxis()  # Inverser l'axe des y pour avoir le plus grand en haut

# Masquer l'axe horizontal (ticks et ligne de l'axe)
plt.gca().xaxis.set_ticks([])  # Masquer les ticks de l'axe des x
plt.gca().spines['bottom'].set_visible(False)  # Masquer la ligne de l'axe des x

# Retirer les bordures haute et droite
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Ajouter plus de marge à droite des barres
max_streams = top_100["Streams"].max()
plt.xlim(0, max_streams * 1.1)  # Ajouter 10% d'espace à droite

# Ajouter le nombre de streams en milliards à la suite des barres
for bar, stream in zip(bars, top_100["Streams"]):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, '{:.2f}B'.format(stream/1e9),
             va='center', ha='left', fontsize=8)

# Ajouter des labels et un titre
plt.xlabel('Nombre de Streams', fontsize=10)  # Label de l'axe des x (visible)
plt.ylabel('Artistes', fontsize=10)
plt.title('Top 100 des artistes par nombre de streams', fontsize=12)

# Réduire la taille de la police des noms des artistes
plt.yticks(fontsize=8)  # Taille de la police pour les noms des artistes

# Ajuster les marges pour optimiser l'espace
plt.tight_layout()

# Sauvegarder en PDF
with PdfPages('/datavolume1/job-exerciceMR-5/outputs/resultat_a4.pdf') as pdf:
    pdf.savefig()

# Fermer la connexion à HBase
connection.close()