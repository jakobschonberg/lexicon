#F1
catalogue = [
    {"type": "book",
     "title": "The Diamond Throne",
     "author": "David Eddings",
     "year": 1989},
    {"type": "movie",
     "title": "Fatal Journey",
     "genres": ["Fantasy", "Action", "Costume & Period"],
     "year": 2020},
     {"type": "game",
      "title": "Trackmania",
      "genre": "racing",  
      "year": 2020},
      {"type": "game",
      "title": "Crusader Kings III",
      "genre": "grand strategy",  
      "year": 2020},
      {"type": "game",
      "title": "Stellaris",
      "genre": "strategy",  
      "year": 2016},
      {"type": "game",
      "title": "Graveyard Keeper",
      "genre": "Simulation",  
      "year": 2018},
      {"type": "game",
      "title": "Warhammer 40,000: Rogue Trader",
      "genre": "RPG",  
      "year": 2023},
      {"type": "game",
      "title": "Solasta",
      "genre": "RPG",  
      "year": 2021}
]
#print(catalogue)

#F2
l = catalogue.copy() #kind of already had the dictionaries in a list, what do you mean??

#F3
types = set([d.get("type") for d in l if "type" in d])
genres = set([d.get("genre") for d in l if "genre" in d]).union(set(*[d.get("genres") for d in l if "genres" in d]))
print(types)
print(genres)

#F4
t = []
for i in l:
    tup = (i["title"],i["year"])
    t.append(tup)
print(t)

#F5
book_titles = [d.get("title") for d in l if "type" in d and d["type"] == "book"]
movie_titles = [d.get("title") for d in l if "type" in d and d["type"] == "movie"]
game_titles = [d.get("title") for d in l if "type" in d and d["type"] == "game"]
print(book_titles)
print(movie_titles)
print(game_titles)
for i in book_titles:
    o = next(x for x in l if x["title"] == i)
    o["pages"] = 496
print(l)
books = (x for x in l if x["type"] == "book")
movies = (x for x in l if x["type"] == "movie")
games = (x for x in l if x["type"] == "game")
print(*books)
print(*movies)
print(*games)
print(l[5]["title"])
print(l[2]["year"])
print(l[-1]["genre"])

#F6
#print(*l[0].values())
#print(*l[1].values())
#print(*l[2].values())
#print(*l[3].values())
#print(*l[4].values())
#print(*l[5].values())
#print(*l[6].values())
#print(*l[7].values())
for i in l:
    print(*i.values())