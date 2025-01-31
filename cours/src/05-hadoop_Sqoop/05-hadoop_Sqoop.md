![diginamic](../img/diginamic.png) ![sqoop](../img/sqoop.png)

<br>

# Sqoop

<br>

## <u>Introduction</u>

Pourquoi Sqoop ?

- En big data, Hadoop est le framework le plus utilisé pour gérer et analyser des données. Cependant, il n’est pas fait pour se connecter directement à des données stockées dans des bases SQL.

- En effet, Hadoop a été conçu pour utiliser d’autres technologies de stockage, telles que HDFS ou Hive. Or, la base SQL reste la solution de stockage la plus répandue…

- Cet outil permettant une cohabitation des bases de données (Oracle, mysql…) avec la plateforme Hadoop (Le nom Sqoop est un mot valise constitué de sql et de hadoop)

- Sqoop permet d’exporter des données depuis la base de données et de procéder aux traitements en exploitant le cluster Hadoop.

- Sqoop est l’outil qui permet de ne pas faire de compromis entre des capacités d’analyses en big data et l’utilisation de bases de données SQL.

- En effet, Sqoop permet de relier un cluster Hadoop à une (ou plusieurs) base(s) de données SQL, en vue de transférer des données de l’un à l’autre, dans les deux sens.

- Il est possible d’exporter le résultat d’un traitement vers une base de données tierce afin qu’il soit exploité par une application (à des fins de restitution par exemple).

- Sqoop a été conçu avec comme objectif principal d’assurer des performances élevées pour ces opérations d’import ou d’export massifs.

**Sqoop prend des données à la source et les écrit dans une destination !!**

<div style="page-break-after: always;"></div>

## <u>Présentation de Sqoop</u>

### **Fonctionnement de Sqoop ?**

Rentrons un peu plus dans le concret. En pratique, Sqoop se présente sous la forme d’une boîte à outils en ligne de commandes, codée en Java et accessible avec la commande sqoop.

Comme nous l’avons dit, Sqoop permet de transférer des données.

on retrouve donc deux outils principaux : `sqoop-import` et `sqoop-export`

![009](009.png)

<br>

### **Import avec Sqoop**

La commande `sqoop-import` permet d’importer des données **d’une base de données SQL vers Hadoop**. Pour utiliser cette commande, vous devez spécifier la base de données SQL d’où les données seront importées.

Sqoop supporte les technologies SQL les plus populaires (mysql, Oracle, PostgreSQL…), mais vous pouvez aussi spécifier un driver particulier via le paramètre —driver.

Sqoop faisant partie d’un framework distribué, plusieurs processus s’exécutent en parallèle pour un même import, rendant le processus très efficace.

Sqoop propose plusieurs paramètres d’import, notamment :

![010](010.png)

Par défaut, Sqoop importe vos données vers un stockage HDFS, mais vous pouvez aussi utiliser d’autres technologies big data comme destination, notamment HBase ou Hive.

![011](011.png)

<br>

### **Export avec Sqoop**

L'outil d'exportation exporte un ensemble de fichiers de HDFS vers un SGBDR avec la commande `sqoop-export`. De la même manière, vous spécifiez une base de données SQL cible.

**À noter que la table dans laquelle vous souhaitez exporter les données doit déjà exister.** Vous pouvez insérer les données (sql INSERT) ou bien mettre à jour des lignes existantes (sql UPDATE).

À l’instar de l’import, de nombreux paramètres d’export existent et l’export est parallélisé pour gagner en efficacité.

![012](012.png)

<br>

### **Plusieurs autres commandes Sqoop utiles**

sqoop-list-databases et sqoop-list-tables pour lister les schémas des bases de données connectées au serveur ainsi que leurs tables.

![013](013.png)

Import-All-Table permet d’importer toutes les tables de la base de données spécifiée.

![014](014.png)

Eval est utilisé pour exécuter des requêtes SQL définies par l'utilisateur sur une base de données et imprimer les résultats sur la console afin qu'un utilisateur puisse examiner le contenu de la table avant d'effectuer l'opération d'importation.

`sqoop eval --connect jdbc:mysql://localhost/userdata?serverTimezone=UTC --username root --password cloudduggu --query "select * from employee";`

`sqoop eval --connect jdbc:mysql://localhost/userdata?serverTimezone=UTC --username root --password cloudduggu --query "update employee set empname='cloudduggu' where empid=1010;"`
