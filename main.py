from conection import *


pesquisas = list(movies.find({

   },{
       "_id" : 0,
       "title" : 1,
       "genres" : 1,       
       "type" : 1,
       "countries" : 1
   }))
                 
print(pesquisas)

with open("Filmes e series", "w", newline='') as movies:
    fieldnames = ['title', 'genres', 'type', 'countries']

    writer = csv.DictWriter(movies, fieldnames=fieldnames)

    writer.writeheader()

    for pesquisa in pesquisas:
        writer.writerow(pesquisa)