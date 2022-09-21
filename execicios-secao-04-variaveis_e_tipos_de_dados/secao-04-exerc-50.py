"""
Exercicios de fixação
"""
# 36
#from datetime import timedelta

import datetime as d


ano_atual = d.datetime.now()
idade = int(input("Digite sua idade: "))
ano_nascimento = ano_atual.year - idade
print(f'Ano de nascimento {ano_nascimento}')
