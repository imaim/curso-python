"""
Exercicios de fixação
"""


# 8- nota entre 0 e 10 com mensagem de nota invalida caso fora no range
valor1 = float(input("Digite a primeira nota: "))
valor2 = float(input("Digite a primeira nota: "))


def validanota(nota):
    if 0 <= nota <= 10:
        return True
    else:
        return False


if validanota(valor1) and validanota(valor2):
    print(f'A média final é {(valor1 + valor2) / 2}')
else:
    if not validanota(valor1) and not validanota(valor2):
        print(f'Ambas as notas são invalidas')
    elif not validanota(valor1):
        print(f'a primeira nota {valor1} é invalida')
    elif not validanota(valor2):
        print(f'a segunda nota {valor2} é invalida')

