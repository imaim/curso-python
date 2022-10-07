"""
Exercicios de fixação
"""
# import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
ano = int(input("Digite o ano: "))
result_ano = ano % 4
result_ano2 = ano % 100
if ano % 4 == 0 and result_ano2 % 100 != 0:
    print("Bisexto")
else:
    print("Nao é bisexto")
