import happybase

# Connection engine Hbase
HOST = 'node188358-env-1839015-hadoop-robin.sh1.hidora.com'
PORT = 11705
connection = happybase.Connection(HOST, PORT)
connection.open()

table_name = "exercice4"
table = connection.table(table_name)

data = table.scan()
cumul = 0
for key, value in data:
    cumul += int(value[b"exo4:streams"])
print(cumul)