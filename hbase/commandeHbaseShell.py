1. Créer la table bibliotheque
create 'bibliotheque', 'auteur', 'livre'


2. Ajouter les données
put 'bibliotheque', 'vhugo', 'auteur:nom', 'Hugo'
put 'bibliotheque', 'vhugo', 'auteur:prenom', 'Victor'
put 'bibliotheque', 'vhugo', 'livre:titre', 'La légende des siècles'
put 'bibliotheque', 'vhugo', 'livre:categ', 'Poemes'
put 'bibliotheque', 'vhugo', 'livre:date', '1855'

put 'bibliotheque', 'jverne', 'auteur:nom', 'Verne'
put 'bibliotheque', 'jverne', 'auteur:prenom', 'Jules'
put 'bibliotheque', 'jverne', 'livre:titre', 'Face au drapeau'
put 'bibliotheque', 'jverne', 'livre:categ', 'Roman'
put 'bibliotheque', 'jverne', 'livre:date', '1896'

3. Afficher toutes les données de la table
scan 'bibliotheque'

4. Afficher la liste des livres stockés pour vhugo
get 'bibliotheque', 'vhugo', {COLUMN => ['livre':titre']}

5. Modifier la date du livre de vhugo pour 2024
put 'bibliotheque', 'vhugo', 'livre:date', '2024'

6. Supprimer livre:categ de vhugo
delete 'bibliotheque', 'vhugo', 'livre:categ'

7. Afficher les livres qui sont sortis après le 20e siècle (après l’an 2000)
scan 'bibliotheque', {FILTER => "SingleColumnValueFilter('livre', 'date', >, 'binary:2000')"}

8. Supprimez toutes les données de jverne
deleteall 'bibliotheque', 'jverne'

Si vous souhaitez supprimer complètement la table :
disable 'bibliotheque'
drop 'bibliotheque'
