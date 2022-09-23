"""
Exercicios de fixação
"""
from math import sqrt as raiz


# 2 - raiz quadrada para valor positivo
valor1 = float(input("Digite o valor: "))

if valor1 > 0:
    print(f'a raiz quadrada do valor {valor1} é {raiz(valor1)}')
else:
    print(f'O maior valor {valor1} é invalido')
