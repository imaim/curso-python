"""
Exercicios de fixação
"""
# 36
#import math

numero_int = str(input("Digite um numero com 4 casas decimais(1000 a 9999): "))
if 1000 <= int(numero_int) <= 9999:
    numero = 0
    while numero < len(numero_int):
        print(f'{numero_int[numero]}')
        numero += 1
else:
    print(f'Valor diferente do range esperado')
