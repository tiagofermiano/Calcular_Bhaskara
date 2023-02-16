import math

#Recebendo os valores de A, B e C
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

#Calculando o Delta

d = (b*b) -4*a*c

#Condição e Calculando o X
if d < 0:
    print("A equação não possui raizes reais!")
if d == 0:
    x1 = ((-b) + math.sqrt(d)) / (2*a)
    print("A equação possui uma raiz real {}!".format(x1))
if d > 0:
    x1 = ((-b) + math.sqrt(d)) / (2*a)
    x2 = ((-b) - math.sqrt(d)) / (2*a)

    print("A equação possui duas raizes reais {:.2f} e {:.2f}!".format(x1,x2))

#O ARQUIVO FOI ALTERADO POR AUGUSTO MEDEIROS
