# 1. Sprawdzianie czy liczba jest pierwsza
# liczby pierwsze - liczba, która się dzieli tylko orzez 1 i samą siebie
# 2,3,5,7,11,13,17,19,23 .. itd.
# Dzielniki właściwe - dzielniki liczb poza 1 nią samą

# n = int(input())
# for i in range(2, n):
#     if  n % i == 0:
#       print("Liczba nie jeast pierwsza")
#       exit(0)
# print("Liczba jest pierwsza")



  
# 2. Generowanie liczb pierwszych NA PAMIĘĆ !!! (w przedziale [p,n])

# n = int(input("Podaj od ilu mam szukać liczb pierwszych"))
# n = int(input("Podaj do ilu mam szukać liczb pierwszych"))

# for i in range(p, n+1):
#   flaga = True;
#   for j in range(2,int(i**0.5)+1):
#     if i % j == 0:
#       flaga = False
#       break
#   if flaga:
#     print(i, end=" ")

# Zad 3. Generownaie liczb pierwszych (pierwsze p liczb pierwszych)
# p = int(input("Podaj do ile (od początku) liczb pierwszych chcesz"))
# i = 2
# licznik = 0

# while 1:
#   flaga = True;
#   for j in range(2,int(i**0.5)+1):
#     if i % j == 0:
#       flaga = False
#       break
#   if flaga == True:
#     print(i, end=" ")
#     licznik += 1
#   if licznik == p:
#     break
#   else:
#     i = i + 1