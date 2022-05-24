def dobro(x):
    return x**2

valor = 2
print(dobro(valor))

valor1 = [1,2,3,4,5]

valor_dobrado = map(dobro,valor1)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)