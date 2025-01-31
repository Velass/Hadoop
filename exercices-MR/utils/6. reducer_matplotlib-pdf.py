###########
# IMPORTS #
###########

import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

######################
# PARTIE AGGREGATION #
######################

current_word = None
current_count = 0
maliste = []  # Liste pour stocker les mots et leurs comptes

# Les données proviennent de l'entrée standard (STDIN)
for line in sys.stdin:
    # Parse l'input recu du mapper.py
    word, count = line.split(';')

    # Protection anti-crash: convertion 'count' en entier
    try:
        count = int(count)
    except ValueError:
        continue

    # Agrégation des mots et comptages
    if current_word == word:
        current_count += count
    else:
        # Protection pour ne pas ajouter 'NONE' qui est le premier mot
        if current_word:
            maliste.append((current_word, current_count)) # Tuple: (mot, count)
            
        # Mettre à jour le mot et le compteur
        current_count = count
        current_word = word

# Ajouter le dernier mot
if current_word == word:
    maliste.append((current_word, current_count))


########################
# PARTIE VISUALISATION #
########################

# Créer un DataFrame avec les mots et leurs comptes
df = pd.DataFrame(maliste, columns=["Word", "Count"])

# Créer une nouvelle figure pour le graphe
plt.figure()

# Créer le graphe pie avec les données
plt.pie(df['Count'], labels=df['Word'], autopct='%1.1f%%', startangle=140)
plt.title("Répartition des mots")

# Enregistrer le graphe au format PDF
with PdfPages('/datavolume1/resultat.pdf') as pdf:
    pdf.savefig()  # Sauvegarder le graphe dans le fichier PDF
