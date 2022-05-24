'Concatenação de Strings'

a = "Lucas"
b = "Reinaldo"

concatenar = a + " " + b
print(concatenar)


'Função Len'
tamanho = len(concatenar)
print(tamanho)

'Navegação por índice'
print(a[2])

print(concatenar[0:4])
print(concatenar[0:])

'Tudo em python é objeto sendo assim, pode-se aplicar metodo'
'Método Lower e Upper'

print(concatenar)
print(concatenar.lower())
print(concatenar.upper())

'Método Strip'
concatenar = a + " " + b + " "
print(concatenar.strip())

"Função Split"
minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split(" ")
print(minha_lista)

'Busca de String'
busca = minha_string.find("rei")
print(busca)

print(minha_string[busca:])

'Método Replace'

minha_string = minha_string.replace("rei", "batman")
print(minha_string)