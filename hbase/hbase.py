
import happybase

# connection = happybase.Connection('node188564-env-1839015-2024-d10-etudiant06.sh1.hidora.com', 12125)
# connection.open()

# bibliotheque = connection.table('bibliotheque')

# print(bibliotheque)

# # data = bibliotheque.scan()
# # print(data)
# for value in bibliotheque.scan():
#     print(value)

# # for key, data in tables.scan():
# #  print key, data
# connection.close()



# import happybase

connection = happybase.Connection('node188564-env-1839015-2024-d10-etudiant06.sh1.hidora.com', 12125)
connection.open()
# connection.create_table('bibliotheque2', {'auteur': dict(), 'livre': dict()})
bibliotheque2 = connection.table('bibliotheque2')

# bibliotheque2.put(b'vhugo', {b'auteur:nom': b'Hugo', 'bauteur:prenom': b'Victor', b'livre:titre': b'La légende des siecles', b'livre:categ': b'Poemes', b'livre:date': b'1855'})
# bibliotheque2.put(b'jverne', {b'auteur:nom': b'Verne', b'auteur:prenom': b'Jules', b'livre:titre': b'Face au drapeau', b'livre:categ': b'Roman', b'livre:date': b'1896'})
# print(bibliotheque2.row(b'vhugo'), )
# for key, value in bibliotheque2.scan():
#     print(key, value)

# bibliotheque2.put(b'vhugo', {b'livre:date': b'2024'})
# bibliotheque2.delete(b'vhugo', columns=[b'livre:categ'])
# bibliotheque2.delete(b'jverne')
# for key, value in bibliotheque2.scan():
#     if value.get(b'livre:date') > b'2000':
#         print(key, value)
        
for element in bibliotheque2.scan(filter="SingleColumnValueFilter('livre', 'date', >, 'binary:1999')"):
    print(element)

connection.close()