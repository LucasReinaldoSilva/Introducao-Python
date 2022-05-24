'Ordenador de Números'

lista = [0,0,0]

lista[0] = int(input("Insira o primeiro número: "))
lista[1] = int(input("Insira o segundo número: "))
lista[2] = int(input("Insira o terceiro número: "))

for i in lista:
    print(i)

lista.sort(reverse=False)

print(lista)