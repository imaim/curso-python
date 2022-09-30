"""
Exercicios de fixação
"""

#import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
valor1 = int(input("Digite a primeira nota: "))
valor2 = int(input("Digite a segunda nota: "))
valor3 = int(input("Digite a terceira nota: "))
resultado = (valor1 * 1 + valor2 * 1 + valor3 * 2) / (1 + 1 + 2)
if resultado <= 60:
    print(f"Aprovado, sua média ponderada é {resultado}")
else:
    print(f"Reprovado, sua média ponderada é {resultado}")

