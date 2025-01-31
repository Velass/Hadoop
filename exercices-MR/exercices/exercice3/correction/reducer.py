import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

data = []
current_year = None
current_streams = 0

for line in sys.stdin:
    year, streams = line.split("\t")
    
    try:
        year = int(year)
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

# trier par rapport au streams décroissant
# tableau_triee = sorted(data, key=lambda x: x[1], reverse=True)
df = df.sort_values(by="Streams", ascending=False)

# afficher sur les 10 premiers
top_10 = df.head(10)

plt.figure()
plt.pie(top_10["Streams"], labels=top_10["Year"], autopct="%1.1f%%", startangle=140)

with PdfPages('resultat.pdf') as pdf:
    pdf.savefig()  # Sauvegarder le graphe dans le fichier PDF

plt.show()