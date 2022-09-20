"""
Exercicios de fixação
"""
# 36
#import math

salario_base = float(input("Digite o salario base: "))
imposto = salario_base * 0.07
salario_final = (salario_base * 1.05) - imposto

print(f'O salario a receber é R$ {salario_final}, foi debitado imposto total de R$ {imposto}')
