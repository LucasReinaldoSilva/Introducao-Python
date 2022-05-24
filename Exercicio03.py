'Cálculo de Equação de segundo grau'

import math

def delta (a,b,c):
    return ((b*b) - (4*a)*(c))

def expxp (a,b,c):
    raizq = math.pow(c, 1/2)
    return ((-b  + raizq))/(2*a)

def expxn (a,b,c):
    raizq = math.pow(c, 1/2)
    return ((-b - raizq)) / (2*a)

elemento1 = float(input("Tendo em vista a seguinte expressçao ?x²+?x+?, insira o valor de x²: "))
elemento2 = float(input("Tendo em vista a seguinte expressçao ?x²+?x+?, insira o valor de x: "))
elemento3 = float(input("Tendo em vista a seguinte expressçao ?x²+?x+?, insira o valor final : "))

try:
    d =  delta(elemento1, elemento2, elemento3)
    eq1 = expxp(elemento1,elemento2,d)
    print(" O valor de x1 é " + str(eq1))
except:
    print("Não foi possivel calcular o valor de x1")

try:
    d = delta(elemento1, elemento2, elemento3)
    eq2 = expxn(elemento1, elemento2,d)
    print("O valor de x2 é " + str(eq2))
except:
    print("Não foi possivel calcular x2")
