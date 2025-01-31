./start-hadoop.sh
./services_hbase_thrift.sh

cat <<CMDES | hbase shell
disable 'maTable'
drop 'maTable' 
exit
CMDES
