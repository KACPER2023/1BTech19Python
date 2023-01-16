# Zad 1

# a = int(input("Podaj Liczbę"))
# b = int(input("Podaj Liczbę"))
# if (a + b) % 2 == 0:
#   print("TAK")
# else:
#   print("NIE")

# Zad 2

# a = int(input("Podaj Liczbę"))
# g = int(input("Podaj Liczbę"))
# if (a + g) / 2 > (a * b)**(1/2):
#   print("TAK")
# else:
#   print("NIE")

# Zad 3

# k = int(input("Podaj Liczbę"))
# l = int(input("Podaj Liczbę"))
# m = int(input("Podaj Liczbę"))
# if k==l or m==k or m==l:
#   if k==l:
#     print("TAK")
#     print(k,l)
#   if m==k:
#     print("TAK")
#     print(m,k)
#   if m==l:
#     print("TAK")
#     print(m,l)
# else:
#   print("NIE")

# Zad 4

a = int(input("Podaj Liczbę"))
b = int(input("Podaj Liczbę"))
c = int(input("Podaj Liczbę"))
d = int(input("Podaj Liczbę"))

if a<b and a<c and a<d:
  print(a)
if b<a and b<c and b<d:
  print(b)
if c<a and c<b and c<d:
  print(c)
if d<a and d<b and d<c:
  print(d)
else:
  print("niema takiej liczby")
  