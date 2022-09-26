"""
Exercicios de fixação
"""


# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
sexo = str(input("Qual o seu sexo ? m > marculino ou f > feminino: "))
altura = float(input("Qual sua altura ? "))
if sexo == "m":
    resultado = (72 * altura) - 58
elif sexo == "f":
    resultado = (62.1 * altura) - 44.7

print(f"o imc é {resultado:.2f}")
