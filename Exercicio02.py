'Média de Notas'

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1+nota2)/2

if media >= 6:
    print("Você foi APROVADO com média " + str(media) +"!!")
else:
    print("Você foi REPROVADO com média " + str(media))