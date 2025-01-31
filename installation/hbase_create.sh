./start-hadoop.sh
./services_hbase_thrift.sh

cat <<CMDES | hbase shell
create 'maTable','cf'
list
describe 'maTable'
put 'maTable','1','cf:a','Test'
exit
CMDES

