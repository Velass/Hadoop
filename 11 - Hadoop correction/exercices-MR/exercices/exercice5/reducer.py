###########
# IMPORTS #
###########

import sys
import happybase
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#############
# HAPPYBASE #
#############

# HOST = '127.0.0.1'
# PORT = 9090
HOST = 'node188358-env-1839015-hadoop-robin.sh1.hidora.com'
PORT = 11705
connection = happybase.Connection(HOST, PORT)
connection.open()

TABLE_NAME = 'exercice5'

try:
    connection.disable_table(TABLE_NAME)
    connection.delete_table(TABLE_NAME)
except Exception:
    pass

cf = {'exo5': dict()}
connection.create_table(TABLE_NAME, cf)
table = connection.table(TABLE_NAME)

###########
# REDUCER #
###########

aggregated = []
current_name = None
current_streams = 0

for line in sys.stdin:
    name, streams = line.split('\t')
    
    try:
        streams = int(streams)
    except:
        continue
    
    if current_name == name:
        current_streams += streams
    else:
        if current_name: # empecher l'insert None (1ere ligne)
            table.put(
                current_name.encode(),
                {
                    b'exo5:streams' : str(current_streams).encode()
                }
            )
            aggregated.append((current_name, current_streams))
        current_name = name
        current_streams = streams
        
if current_name: # empecher l'insert None (1ere ligne) // insertion de la derniere ligne
    table.put(
        current_name.encode(),
        {
            b'exo5:streams' : str(current_streams).encode()
        }
    )
    aggregated.append((current_name, current_streams))
    
#################
# VISUALISATION #
#################

df = pd.DataFrame(aggregated, columns=["artist_name", "streams"])
df = df.sort_values(by="streams", ascending=False)
top_100 = df.head(100)

plt.figure()
plt.barh(top_100["artist_name"], top_100["streams"])
plt.gca().invert_yaxis()
plt.title("Top 100 des artites par streams")
plt.xlabel("Nombre de streams")
plt.ylabel("Nom de l'artiste")
plt.tight_layout()

with PdfPages("resultat.pdf") as pdf:
    pdf.savefig()
    
plt.show()

connection.close()