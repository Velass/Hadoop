import happybase

# connection = happybase.Connection('127.0.0.1', 9090)
connection = happybase.Connection('node188358-env-1839015-hadoop-robin.sh1.hidora.com', 11705)
connection.open()

# 1. Create table 'bibliotheque', with column family 'livre' et 'auteur'
table_name = 'bibliotheque2'

try:
    connection.disable_table(table_name)
    connection.delete_table(table_name)
except:
    pass

connection.create_table(
    table_name,
    {
        'livre': dict(),
        'auteur': dict()
    }
)

# Se déplacer dans la table
table = connection.table('bibliotheque')

# 2. insérer des données
table.put(
    b'vhugo',
    {   
        # 'cf:col': 'val'
        b'auteur:nom': 'Hugo'.encode(),
        b'auteur:prenom': 'Victor'.encode(),
        b'livre:titre': b'La legende des siecles',
        b'livre:categ': b'Poemes',
        b'livre:date': b'1855',
    }
)

table.put(
    b'jverne',
    {   
        # 'cf:col': 'val'
        b'auteur:nom': 'Verne'.encode(),
        b'auteur:prenom': 'Jules'.encode(),
        b'livre:titre': b'Face au drapeau',
        b'livre:categ': b'Roman',
        b'livre:date': b'1896',
    }
)

# Afficher toutes les données de la table.
# for key, value in table.scan():
#     print(key, value)

# 4. Afficher la liste des livres stockés pour vhugo.
# print(table.row(b'vhugo'))

# 5. Modifier la date du livre de 'vhugo' pour 2024.
table.put(
    b'vhugo',
    {
        b'livre:date': b'2024'
    }
)

# 6. Supprimer 'livre:categ' de 'vhugo'.
table.delete(b'vhugo', [b'livre:categ'])

# 7. Afficher les livres qui sont sortis après le 20e siècle.
# for element in table.scan(filter="SingleColumnValueFilter('livre', 'date', >, 'binary:1999')"):
#     print(element)
    
# 8. Supprimez toutes les données de 'jverne'
table.delete(b'jverne')
for element in table.scan():
    print(element)

connection.close()