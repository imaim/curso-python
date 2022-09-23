"""
Exercicios de fixação
"""
from math import sqrt as raiz


# 3 - raiz quadrada para valor positivo e potencia de 2 para negativo
valor1 = float(input("Digite o valor: "))

if valor1 > 0:
    print(f'a raiz quadrada do valor {valor1} é {raiz(valor1)}')
else:
    print(f'O valor {valor1} elevado ao quadrado é {valor1 ** 2} ')
