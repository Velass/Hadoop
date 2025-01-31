#!/usr/bin/env python
# -*- coding: utf-8 -*-

import happybase

def add_book(table, row_key, nom, prenom, titre, categ, date):
    table.put(
        row_key.encode('utf-8'),
        {
            b'auteur:nom': nom.encode('utf-8'), 
            b'auteur:prenom': prenom.encode('utf-8'),
            b'livre:titre': titre.encode('utf-8'),
            b'livre:categ': categ.encode('utf-8'),
            b'livre:date': date.encode('utf-8')
        }
    )
    
# Connexion à HBase en localhost
connection = happybase.Connection('127.0.0.1', port=9090)
connection.open()

# 1. Créer la table si nécessaire
connection.create_table(
    'bibliotheque',
    {
        'auteur': dict(),
        'livre': dict()
    }
)

# Récupération de la table bibliotheque
table = connection.table('bibliotheque')

# 2. Ajouter des enregistrements
add_book(table, 'vhugo', 'Hugo', 'Victor', 'La legende des siecles', 'Poemes', '1855')
add_book(table, 'jverne', 'Verne', 'Jules', 'Face au drapeau', 'Roman', '1896')

# 3. Afficher toutes les données de la table
print('Affichage de la table :')
for key, data in table.scan():
    print(key, data)

# 4. Afficher la liste des livres stockés pour vhugo
print('\nAffichage des livres de Victor Hugo :')
print(table.row(b'vhugo'))

# 5. Modifier la date du livre de vhugo pour 2024
table.put(b'vhugo', {b'livre:date': b'2024'})

# 6. Supprimer livre:categ de vhugo
table.delete(b'vhugo', columns=[b'livre:categ'])

# 7. Afficher les livres qui sont sortis après la fin du 20e siècle
print('\nAffichage des livres sortis apres 2000 :')
for key, data in table.scan(filter="SingleColumnValueFilter('livre', 'date', >, 'binary:2000')"):
    print(key, data)

# 8. Supprimez toutes les données de jverne
table.delete(b'jverne')

connection.close()
