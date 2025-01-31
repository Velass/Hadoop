import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MaxNLocator, FuncFormatter

current_year = None
current_streams = 0
data = []

# Traitement des données
for line in sys.stdin:
    year, streams = line.split("\t")
    
    try:
        streams = int(streams)
    except:
        continue
    
    if current_year == year:
        current_streams += streams
    else:
        if current_year:
            data.append((current_year, current_streams))
        current_year = year
        current_streams = streams

if current_year:    
    data.append((current_year, current_streams))
    
#################
# VISUALISATION #
#################

df = pd.DataFrame(data, columns=["Year", "Streams"])

# Créer une nouvelle figure pour le graphe
plt.figure(figsize=(10, 6))  # Ajuster la taille de la figure pour plus de place

# Créer le graphe avec plt.plot()
plt.plot(df["Year"], df["Streams"], marker='o', linestyle='-', color='b')

# Ajouter un titre
plt.title("Répartition des streams par années")

# Formatage des ticks de l'axe Y pour éviter la notation scientifique
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True, prune='both'))  # Utilise des nombres entiers
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))  # Affiche avec des séparateurs de milliers

# Ajuster les ticks de l'axe X (années) pour éviter la superposition
plt.xticks(rotation=60, ha="right")  # Augmenter la rotation des labels des années à 60°

# Ajuster l'échelle de l'axe Y si nécessaire
plt.ylim(0, df["Streams"].max() * 1.1)  # Ajouter un peu d'espace au-dessus des données

# Ajouter des labels aux axes
plt.xlabel("Année")
plt.ylabel("Nombre de streams")

# Enregistrer le graphe au format PDF
with PdfPages('resultat.pdf') as pdf:
    pdf.savefig()  # Sauvegarder le graphe dans le fichier PDF

# Afficher le graphe
plt.tight_layout()  # Ajuste la mise en page pour éviter que les labels soient coupés
plt.show()