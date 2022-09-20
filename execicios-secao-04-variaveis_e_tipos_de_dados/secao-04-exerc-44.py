"""
Exercicios de fixação
"""
# 36
#import math

valor_degral = float(input("Digite a altura do degrau em cm: "))
valor_total_escada = float(input("Digite a altura a ser alcançada em Metros: "))
resultado = (valor_total_escada * 100) / valor_degral

print(f"O Total de degraus a subir é {resultado}")
