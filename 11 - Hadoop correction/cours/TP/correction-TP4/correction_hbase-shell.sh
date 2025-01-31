#1 =>  namespace default
create 'bibliotheque', 'auteur', 'livre'
# namespace 'toto'
create 'toto:bibliotheque', 'auteur', 'livre'

#2
put 'bibliotheque', 'vhugo', 'auteur:nom', 'Hugo'
put 'bibliotheque', 'vhugo', 'auteur:prenom', 'Victor'
put 'bibliotheque', 'vhugo', 'livre:titre', 'La legende des siecles'
put 'bibliotheque', 'vhugo', 'livre:categ', 'Poemes'
put 'bibliotheque', 'vhugo', 'livre:date', '1855'

put 'bibliotheque', 'jverne', 'auteur:nom', 'Verne'
put 'bibliotheque', 'jverne', 'auteur:prenom', 'Jules'
put 'bibliotheque', 'jverne', 'livre:titre', 'Face au drapeau'
put 'bibliotheque', 'jverne', 'livre:categ', 'Roman'
put 'bibliotheque', 'jverne', 'livre:date', '1896'

#3
scan 'bibliotheque'

#4
get 'bibliotheque', 'vhugo', {COLUMNS => ['livre:titre']}

#5
put 'bibliotheque', 'vhugo', 'livre:date', '2024'

#6
delete 'bibliotheque', 'vhugo', 'livre:categ'

#7
scan 'bibliotheque', {FILTER => "SingleColumnValueFilter('livre', 'date', >, 'binary:1999')"}

#8
deleteall 'bibliotheque', 'jverne'