docker container prune
docker rm -f hadoop-master
docker rm -f hadoop-slave1
docker rm -f hadoop-slave2
docker volume prune
docker volume rm digi01
docker volume create digi01
docker network create --driver=bridge hadoop
docker run -v digi01:/datavolume1 -itd --net=hadoop -p 9090:9090 -p 9091:9091 -p 9070:50070 -p 8088:8088 -p 7077:7077 -p 16010:16010 --name hadoop-master --hostname hadoop-master liliasfaxi/spark-hadoop:hv-2.7.2 
docker run -v digi01:/datavolume1 -itd --net=hadoop -p 8040:8042 --name hadoop-slave1 --hostname hadoop-slave1 liliasfaxi/spark-hadoop:hv-2.7.2 
docker run -v digi01:/datavolume1 -itd --net=hadoop -p 8041:8042 --name hadoop-slave2 --hostname hadoop-slave2 liliasfaxi/spark-hadoop:hv-2.7.2 

docker cp happybase.sh hadoop-master:/root
docker cp hbase_create.sh hadoop-master:/root
docker cp hbase_drop.sh hadoop-master:/root
docker cp setup.sh hadoop-master:/root
docker cp hbase_odbc_rest.sh hadoop-master:/root
docker cp services_hbase_thrift.sh hadoop-master:/root

docker cp services_hbase_thrift.sh hadoop-slave1:/root
docker cp services_hbase_thrift.sh hadoop-slave2:/root
docker cp setup.sh hadoop-slave1:/root
docker cp setup.sh hadoop-slave2:/root

docker exec hadoop-master /bin/bash -c './setup.sh'
docker exec hadoop-slave1 /bin/bash -c './setup.sh'
docker exec hadoop-slave2  /bin/bash -c './setup.sh'


