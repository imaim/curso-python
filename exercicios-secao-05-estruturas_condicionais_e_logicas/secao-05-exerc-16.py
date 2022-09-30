"""
Exercicios de fixação
"""
from re import match

#import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
valor = int(input("Digite um numero de 1 a 12: "))

match str(valor):
    case "1":
        print(f'o mes correspondente ao numero {valor} é Janeiro')
    case "2":
        print(f'o mes correspondente ao numero {valor} é Fevereiro')
    case "3":
        print(f'o mes correspondente ao numero {valor} é Março')
    case "4":
        print(f'o mes correspondente ao numero {valor} é Abril')
    case "5":
        print(f'o mes correspondente ao numero {valor} é Maio')
    case "6":
        print(f'o mes correspondente ao numero {valor} é Junho')
    case "7":
        print(f'o mes correspondente ao numero {valor} é Julho')
    case "8":
        print(f'o mes correspondente ao numero {valor} é Agosto')
    case "9":
        print(f'o mes correspondente ao numero {valor} é Setembro')
    case "10":
        print(f'o mes correspondente ao numero {valor} é Outubro')
    case "11":
        print(f'o mes correspondente ao numero {valor} é Novembro')
    case "12":
        print(f'o mes correspondente ao numero {valor} é Dezembro')
    case _:
        print(f'Valor não corresponde ao intervalo informado')
