"""
Exercicios de fixação
"""
from re import match

# import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.

valor = int(input("Digite o numero: "))

div3 = valor % 3
div5 = valor % 5

if (div3 == 0) and (div5 != 0):
    print(f'Valor divisivel por 3')
elif (div5 == 0) and (div3 != 0):
    print(f'Valor divisivel por 5')
else:
    print(f'Valor divisivel por ambos, falha')
