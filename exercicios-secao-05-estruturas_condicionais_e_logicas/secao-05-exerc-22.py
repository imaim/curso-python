"""
Exercicios de fixação
"""
# import math

# 9 - valor do salario e prestação empresitivmo, se prestação maior q 20 % emprestimoo negado.
idade = int(input("Digite a idade: "))
temposerv = int(input("Digite o tempo de serviço(em anos trabalhados): "))

if (idade >= 65 or temposerv >= 30) or (idade >= 60 and temposerv >= 25):
    print("Pode se aposentar")
else:
    print("nao pode se aposentar")
