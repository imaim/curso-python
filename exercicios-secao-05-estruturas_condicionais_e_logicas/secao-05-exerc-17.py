"""
Exercicios de fixação
"""
from re import match

#import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
base1 = float(input("Digite o valor primeira base: "))
base2 = float(input("Digite o valor segunda base: "))
altura = float(input("Digite o valor da altura: "))

if (base1 < 0) and (base2 > 0):
    resultado = ((base1 + base2) * altura) / 2
    print(f'A area do Trapézio é igual a {resultado}')
else:
    print(f'Base com valor abaixo ou igual a 0')
