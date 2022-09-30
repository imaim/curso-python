"""
Exercicios de fixação
"""
from re import match

# import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
selecao = float(input("Selecione a operação desejada:\n"
                       "1 -> Multiplicação\n"
                       "2 -> Divisâo\n"
                       "3 -> Adição\n"
                       "4 -> Subtração\n"
                       ": "))


def resultado(valor1, valor2, operacao):
    if operacao == 1:
        operacao_nome = "Multiplicação"
        calculo = valor1 * valor2
        print(f'O resultado da {operacao_nome} entre {valor1} e {valor2} é {calculo}')
    elif operacao == 2:
        operacao_nome = "Divisâo"
        calculo = valor1 / valor2
        print(f'O resultado da {operacao_nome} entre {valor1} e {valor2} é {calculo}')
    elif operacao == 3:
        operacao_nome = "Adição"
        calculo = valor1 + valor2
        print(f'O resultado da {operacao_nome} entre {valor1} e {valor2} é {calculo}')
    elif operacao == 4:
        operacao_nome = "Subtração"
        calculo = valor1 - valor2
        print(f'O resultado da {operacao_nome} entre {valor1} e {valor2} é {calculo}')


numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))

resultado(numero1, numero2, selecao)
