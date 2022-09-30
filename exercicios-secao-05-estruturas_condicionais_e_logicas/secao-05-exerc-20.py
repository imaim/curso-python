"""
Exercicios de fixação
"""
from re import match

# import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
from math import sqrt as raiz

valor1 = float(input('Informe o primeiro lado em centimetros'))
valor2 = float(input('Informe o segundo lado em centimetros'))
valor3 = float(input('Informe o terceiro lado em centimetros'))

if (valor1 < (valor2 + valor3)) or (valor2 < (valor1 + valor3)) or (valor3 < (valor1 + valor2)):
    if valor1 == valor2 == valor3:
        resutado = (valor1 ** 3) * raiz(3)
        print(f'tringulo equilatero com area igual a {resutado:.2f}')
    if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        print(f'tringulo isóceles')
    elif valor1 != valor2 != valor3 != valor1:
        semiperi = (valor1 + valor2 + valor3) / 2
        resutado = raiz((semiperi * (semiperi - valor1) * (semiperi - valor2) * (semiperi - valor3)))
        print(f'tringulo escaleno com area igual a {resutado:.2f}')
else:
    print(f'Valores invalidos para um lado de um triangulo')