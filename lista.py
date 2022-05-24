minha_lista= ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["Ola", 2, 9.78, True]

print(minha_lista[2])

for item in minha_lista:
    print(item)


tamanho = len(minha_lista)
print(tamanho)


minha_lista.append("limao")

del minha_lista[2:]

print(minha_lista)


'Ordenar Lista'

lista = [124, 345, 5, 73, 46, 6, 7, 3, 1, 7,0]
lista.sort(reverse = False)
print(lista)


lista2 = ["bola", "abacate", "dinheiro"]
lista2.sort(reverse = True)
print(lista2)