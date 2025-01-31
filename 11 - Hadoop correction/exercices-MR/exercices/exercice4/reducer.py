import sys
import happybase

#############
# HAPPYBASE #
#############

# Connection engine Hbase
HOST = 'node188358-env-1839015-hadoop-robin.sh1.hidora.com'
PORT = 11705
connection = happybase.Connection(HOST, PORT)
connection.open()

# Suppression de l'ancienne base de donnée (TABLE)
table_name = "exercice4"
try:
    connection.disable_table(table_name)
    connection.delete_table(table_name)
except:
    pass

# Connection à la base donnée (TABLE)
cf = {"exo4": dict()}
connection.create_table(table_name, cf)
table = connection.table(table_name)

###########
# REDUCER #
###########

current_year = None
current_streams = 0

for index, line in enumerate(sys.stdin):
    year, streams = line.split("\t")
    
    try:
        streams = int(streams)
    except:
        continue
    
    if current_year == year:
        current_streams += streams
    else:
        if current_year:
            # print("%s\t%s" % (current_year, current_streams))
            table.put(
                str(index).encode(),
                {
                    b'exo4:year': current_year.encode(),
                    b'exo4:streams': str(current_streams).encode()
                }
            )
        current_year = year
        current_streams = streams

if current_year:    
    table.put(
        str(index).encode(),
        {
            b'exo4:year': current_year.encode(),
            b'exo4:streams': str(current_streams).encode()
        }
    )
    
connection.close()