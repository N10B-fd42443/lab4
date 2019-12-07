n = input("Wprowadz numer liczby fib: ")

lista = [0,1]

while lista.__len__()<n:
    lista.append(lista[-1]+lista[-2])


print(lista[-1])