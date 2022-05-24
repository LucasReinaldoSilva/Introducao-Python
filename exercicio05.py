x = int(input("Insira o primeiro número da expressão: "))
y = int(input("Insira o segundo número da expressão: "))

print("Escolha  o operador da expressão, sendo que: ")
z = int(input("1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão: "))

if z == 1:
    op = x+y
if z == 2:
    op = x-y
if z == 3:
    op = x*y
if z == 4: 
    op = x/y

if (z<1) or (z>4):
    print(" Escolha um valor válido") 

try:
    print("O valor da operação é " + str(op))
except:
    print("Não foi possivel solucionar a expressão")