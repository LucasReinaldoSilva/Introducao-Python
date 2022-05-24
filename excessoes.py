from ast import Try
from xml.sax.handler import property_interning_dict


a = 2
b = 0

try:
    print(a/b)
except:
    print("Não é permitido divisão por 0")

print(" Deu certo!")