import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import FuncFormatter

years = []
streams = []

current_year = None
current_stream = 0

for line in sys.stdin:
    year, stream = line.split("\t")
    
    try:
        stream = int(stream)
        year = int(year)
    except:
        continue
    
    if current_year == year:
        current_stream += stream
    else:
        if current_year:
            print("%s\t%s" % (current_year, current_stream))
            years.append(current_year)
            streams.append(current_stream)
    
    current_year = year
    current_stream = stream

if current_year:    
    print("%s\t%s" % (current_year, current_stream))
    years.append(current_year)
    streams.append(current_stream)
    
# matplotlib
max_stream = max(streams)
max_year = max(years)
print(max_year)
print(streams)
def format_func(value, tick_position):
    return '{:,}'.format(int(value))  # Affiche avec des séparateurs de milliers

plt.figure(figsize=(12, 6))
plt.plot(years, streams, label="Total Streams")
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_func))
plt.xlabel("Année")
plt.ylabel("Nombre de Streams")
plt.title("Total des Streams par Année")
plt.yticks(list(plt.yticks()[0]) + [max_stream])
plt.ylim(0, max_stream * 1.1 )
 

# # Enregistrer le graphe au format PDF
with PdfPages('exercices-MR\exercices\exercice3\exercice3.pdf') as pdf:
    # with PdfPages('/datavolume1/resultat.pdf') as pdf: permet de sauvegarder le graphe dans un fichier PDF sur la vm
    pdf.savefig()  # Sauvegarder le graphe dans le fichier PDF
    
plt.show()

