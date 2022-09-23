"""
Exercicios de fixação
"""
from math import sqrt as raiz


# 4 - raiz quadrada para valor positivo e potencia ao quadrado
valor1 = float(input("Digite o valor: "))

if valor1 > 0:
    print(f'a raiz quadrada do valor {valor1} é {raiz(valor1)} é elevado ao quadrado é {valor1 ** 2}')
else:
    print(f'O maior valor {valor1} é invalido')
