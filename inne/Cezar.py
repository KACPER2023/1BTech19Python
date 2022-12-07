# Funkcja ord() - zwraca kod ASCII znaku
# print(ord("A"))
# print(ord("Z"))
# w Pythonie kod ASCII wielkich liter A - Z są od 65 do 90

# Funkcja chr() - zwraca znak dla danego kodu
# print(chr(66))
# print(chr(75))

# Zadanie tekstowe: wypisz alfabet liter wielkich

# for i in range(0,200):
#   print(chr(i), end= " ")

# String w pythonie - "lista

# napis = "ARGENTYNA"
# print(napis[0], napis[1], napis[2])


# for i in range(len(napis)):
#   print(napis[i])

# napis = "KOT"
# szyfr = ""
# print(napis[0], napis[1], napis[2])
# print(len(napis)):

# for i in range(len(napis)):
#   print(napis[i])
#   szyfr = szyfr + chr(ord(napis[i])+3)
# print(szyfr)


#   for i in range(len(napis)):
#     szyfr = szyfr + chr(65 +((ord(napis[i])-65+3) % 26))
# print(szyfr)