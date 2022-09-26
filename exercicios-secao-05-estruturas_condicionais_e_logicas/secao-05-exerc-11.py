"""
Exercicios de fixação
"""


# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
valor = str(input("Digite um numero: "))

if 0 < int(valor) < 100:
    resultado = int(valor[0]) + int(valor[1])
elif 100 <= int(valor) < 1000:
    resultado = int(valor[0]) + int(valor[1]) + int(valor[2])
else:
    print("Valor invalido")

print(f"A soma dos algarismos do numero {valor} é {resultado}")
