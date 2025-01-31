./start-hadoop.sh
./services_hbase_thrift.sh

cat <<MOCODE | /usr/bin/python3
import happybase
connection = happybase.Connection('127.0.0.1',9090)
table = connection.table('maTable')
row = table.row(b'1')
data = row[b'cf:a']
print('%s' % data)
MOCODE

