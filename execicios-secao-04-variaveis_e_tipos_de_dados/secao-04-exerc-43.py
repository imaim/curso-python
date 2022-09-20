"""
Exercicios de fixação
"""
# 36
#import math

valor_inicial = float(input("Digite o valor total: "))
valor_total = valor_inicial * 0.90
valor_parcela = valor_inicial / 3
valor_comissao = valor_total * 0.05
valor_comissao_avista = valor_inicial * 0.05

print(f'Valor a Pagar R$: {valor_total}\nValor da parcela, 3x de R$: {valor_parcela:.2f}\nValor Comissao a Prazo R$: {valor_comissao}\nValor Comissao a vista R$: {valor_comissao_avista}')
