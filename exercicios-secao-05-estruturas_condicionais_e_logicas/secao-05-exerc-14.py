"""
Exercicios de fixação
"""

#import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
valor_tl = int(input("Digite a nota do trabalho de laboratório: "))
valor_avs = int(input("Digite a nota da avaliação semestral: "))
valor_exf = int(input("Digite a nota do exame final: "))
resultado = ((valor_tl * 2) + (valor_avs * 3) + (valor_exf * 5)) / (2 + 3 + 5)

if (0 < valor_tl <= 10) and (0 < valor_avs <= 10) and (0 < valor_exf <= 10):
    if 0 < resultado <= 2.9:
        print(f"Reprovado, sua média final é {resultado}")
    elif 3 <= resultado <= 4.9:
        print(f"Recuperação, sua média final é {resultado}")
    else:
        print(f"Aprovado, sua média final é {resultado}")
else:
    print(f"Valor de nota invalido")
