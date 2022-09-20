"""
Exercicios de fixação
"""
# 36
from datetime import timedelta


valor_total_seg = int(input("Digite o valor total em segundos: "))
print(f'O resultado em Horas:minutos:segundos é: {timedelta(seconds=valor_total_seg)}')