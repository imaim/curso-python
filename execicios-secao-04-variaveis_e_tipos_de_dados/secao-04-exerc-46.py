"""
Exercicios de fixação
"""
# 36
#import math

numero_int = str(input("Digite um numero com 3 casas decimais: "))
if int(numero_int) >= 100:
    print(f'numero invertido: {numero_int[::-1]}')
else:
    print(f'Valor menor que o esperado')
