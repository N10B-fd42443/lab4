n = input("Wprowadz numer liczby fib: ")

lista = [0,1]

while lista.__len__()<n:
    lista.append(lista[-1]+lista[-2])


print(lista[-1])


import sys

n = input("Wprowadz numer liczby fib: ")
n = float(n)

z = input("Wprowadz sposob rozwiazania \n 1.iteracyjne \n 2.rekurencyjne \n :")



def rekurencyjne(n):
    lista = [0, 1]
    while lista.__len__()<n:
        lista.append(lista[-1]+lista[-2])
    print(lista[-1])
def iteracyjne(n):

    if n == 1:
        print("0")
        sys.exit()
    if n == 2:
        print("1")
        sys.exit()
    a = 0
    b = 1
    while n / 2 > 1:
        a = a + b
        b = a + b
        n = n - 1
        print(a, b)
    if n % 2 == 0:
        print(a)
    else:
        print(b)
if z == 1:
    iteracyjne(n)
if z == 2:
    rekurencyjne(n)
    
a = input("Wprowadz liczbe a: ")
b = input("Wprowadz liczbe b: ")
a = float(a)
b = float(b)
if x == 1:
    print('Wynik = ', a+b)
if x == 2:
    print('Wynik = ', a-b)
if x == 3:
    print('Wynik = ', a*b)
if x == 4:
    if b == 0:
        print('Blad! Nie mozna dzielic przez 0')
    else:
        print('Wynik = ', a/b)
if x>4:
    print("Niewlasciwy zakres wyboru")
