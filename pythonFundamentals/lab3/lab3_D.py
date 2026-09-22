#D1
for i in range(10, 0, -1):
    print(i)

#D2
number = 7 #number = int(input())
for i in range(1, 11):
    print(number * i)

#D3
tracks = ["The Ides Of March", "Wrathchild", "Murders In The Rue Morgue",
          "Another Life", "Genghis Khan", "Innocent Exile", "Killers",
          "Prodical Son", "Purgatory", "Drifter"]
for number, track in enumerate(tracks):
    print (number + 1, track)

#D4
for y in range(1,5):
    s = ""
    for x in range(1,4):
        s = s + " (" + str(x) + ", " + str(y) +")"
    print(s)

#D5
for y in range(5):
    s = ""
    for x in range(5):
        s = s + chr(x + y*5 + ord('a'))
    print(s)
