![diginamic](../img/diginamic.png) ![sqoop](../img/sqoop.png)

<br>

# TP n°05 : SQOOP

<br>

## <u>Table des matières</u>

- [I. Objectif du TP](#i-objectif-du-tp)
- [II. Démarrer avec Sqoop](#ii-démarrer-avec-sqoop)
   - [A. Installation et configuration de SQOOP (Linux)](#a-installation-et-configuration-de-sqoop-linux)
   - [B. Installation et configuration de MySQL (Linux)](#b-installation-et-configuration-de-mysql-linux)
   - [C. Création d’une Base de données sur MySQL](#c-création-dune-base-de-données-sur-mysql)
- [III. Exercice suite au TP](#iii-exercice-suite-au-tp)

<div style="page-break-after: always;"></div>

## <u>I. Objectif du TP</u>

- Initiation à l’outil Sqoop.

<br>

## <u>II. Démarrer avec Sqoop</u>

### **A. Installation et configuration de SQOOP (Linux)**

1. Télécharger le package Sqoop (la version 1.4.7) :

   - wget [https://archive.apache.org/dist/sqoop/1.4.2/sqoop-1.4.2.tar.gz](https://archive.apache.org/dist/sqoop/1.4.2/sqoop-1.4.2.tar.gz)

2. Décompresser le fichier et le déplacer dans le répertoire /usr/local

   - tar -xvf sqoop-1.4.2.tar.gz
   - mv /usr/local/sqoop-1.4.2 /usr/local/sqoop

3. Ajouter les variables nécessaires sur l’env :

   - vi .bashrc
   - export SQOOP_HOME=/usr/local/sqoop  export PATH=$PATH:$SQOOP_HOME/bin  source .bashrc

4. Configurer Sqoop:

   - cd $SQOOP_HOME/conf
   - mv sqoop-env-template.sh sqoop-env.sh   vi sqoop-env.sh

5. sur le fichier ajouter les deux chemins Hadoop : (echo $HADOOP_HOME) et Hbase (echo $HBASE_HOME)

   - export HADOOP_COMMON_HOME=/usr/local/Hadoop
   - export HADOOP_MAPRED_HOME=/usr/local/Hadoop

6. Configurer le sqoop jar dans sqoop home :

   - wget https://repo1.maven.org/maven2/org/apache/sqoop/sqoop/1.4.2/sqoop-1.4.2-hadoop200.jar
   - cp sqoop-1.4.2-hadoop200.jar  $SQOOP_HOME

7. Configurer le connecteur mysql :

   - wget http://ftp.ntu.edu.tw/MySQL/Downloads/Connector-J/mysql-connector-java-8.0.29.tar.gz
   - tar -xvf mysql-connector-java-8.0.29.tar.gz
   - mv mysql-connector-java-8.0.29/mysql-connector-java-8.0.29.jar /$SQOOP_HOME/lib

8. Vérifier l’installation de Sqoop :

   - cd $SQOOP_HOME/bin sqoop version

   ![004](004.png)

<br>

### **B. Installation et configuration de MySQL (Linux)**

Afin d’utiliser Sqoop, on va créer une base de données sur Mysql pour pouvoir la migrée sur HDFS. Decoup, on va commencer par installer Mysql :

1. Installation de Mysql

   - apt update
   - apt install mysql-server mysql -V

2. Lancer Mysql

   - service mysql start mysql -u root -p

<br>

### **C. Création d’une Base de données sur MySQL**

On va créer une base de données « movies », utilisez le fichier movies.sql. Excecuter les commandes sql sur le mysql shell.

1. Vérifiez que la base de données est bien crée
2. Affichez "movie_id, title, budget, revenue, popularity, vote_count" pour chaque film.
3. Afficher la liste des films qui ont apporté des revenues par order de vote.

<div style="page-break-after: always;"></div>

## <u>III. Exercice suite au TP</u>

1. Afficher la liste des bases de données disponibles sur notre serveur MySQL.
2. Afficher la liste des tables disponibles sur notre serveur MySQL pour la base de données movies.
3. Afficher le résultats de la requête qui permet d’afficher "movie_id, title, budget, revenue, popularity, vote_count" pour chaque film.
4. Importez toute la table movie dur HDFS.
5. Vérifier que les données sont bien importées sur HDFS.
6. Importez sur HDFS le résultat pour la requête qui permet d’afficher la liste des films qui ont apporté des revenues ordonnées par vote en utilisant sqoop.
7. Vérifier que les données sont bien importées sur HDFS.
8. Exporter les données stockées sur HDFS pour la partie salaire (age, max salaire, minsalaire, nombre) vers le mysql.
