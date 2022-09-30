"""
Exercicios de fixação
"""
from re import match

#import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
valor = int(input("Digite um numero de 1 a 7: "))

match str(valor):
    case "1":
        print(f'o dia correspondente ao numero {valor} é Domingo')
    case "2":
        print(f'o dia correspondente ao numero {valor} é Segunda-feira')
    case "3":
        print(f'o dia correspondente ao numero {valor} é Terça-feira')
    case "4":
        print(f'o dia correspondente ao numero {valor} é Quarta-feira')
    case "5":
        print(f'o dia correspondente ao numero {valor} é Quinta-feira')
    case "6":
        print(f'o dia correspondente ao numero {valor} é Sexta-feira')
    case "7":
        print(f'o dia correspondente ao numero {valor} é Sabado')
    case _:
        print(f'Valor não corresponde ao intervalo informado')
