"""
Exercicios de fixação
"""

import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
valor = int(input("Digite um numero: "))

if 0 < valor:
    resultado = math.log(valor)
    print(f"A soma dos algarismos do numero {valor} é {resultado}")
else:
    print("Valor invalido")

