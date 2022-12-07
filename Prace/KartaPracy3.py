# PRE

# print(list(range(2, 8, 1)))

# print(list(range(1, 8, 2)))

# print(list(range(10)))

# Zad pętla liczb dwucyfrowych od 10 do 21

# for (i) in range(10,22):
#   print(i)

# Zad pętla liczb dwucyfrowych nieparzystych od 15 do 31

# for (i) in range(15, 32, 2):
#   print(i)

# Zad pętla liczb dwucyfrowych malejąco (step ujemny)

# for (i) in range(99,9 -1):
#   print(i, end=" ")

# Zad pętla liczb dwucyfrowych malejąco(step dodatni)

# for (i) in range(10, 100, 1):
#   print(109-i, end=" ")

# Zad pętla liczb 3-cyfrowych podzielna przez 20

# for (i) in range(100, 981, 20):
#   print(i, end=" ")

# Zad 1

# n = int(input())

# for (i) in range(n):
#   print(i**3 + 3, end=" ")

# Zad 2

# for (i) in range(105, 991, 15):
#   print(i, end=" ")

# Zad 3

# p = int(input())

# for (i) in range(1, p + 1):
#   if p % i == 0:
#     print(i)

# Zad 4

# a = 0

# for i in range(10, 100):
#   a = a + i 
# print(a)

# Zad 5

# n = int(input("w ile gramy?"))

# suma = n * (n+1)  // 2
# for i in range(n-1):
#   a = int(input())
#   suma = suma - a
# print("Brakuje:", suma)

# Zad Dodatokowe - napisz pętle sumującą liczby dwucyfrowe parzyste

# suma = 0
# for i in range(10, 100, 2):
#   suma = suma + n
# print(suma)

# Zad 6
# Fibo według literatury 0 1 1 2 3 5 8 13 ...
# Fibo nasze: 1, 2, 3, 5, 8, ...

# n = int(input())
# a, b = 0, 1
# for i in range(n):
#   a, b = b, a + b
#   print(b)