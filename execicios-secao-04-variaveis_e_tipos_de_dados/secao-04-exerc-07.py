"""
Exercicios de fixação
"""
# 5 - receber 1 valor real e imprimir a quinta parte dele

valor_fahrenheit = float(input("Digite a Temperatura em Fahrenheit: "))
valor_celsius = 5 * (valor_fahrenheit - 32) / 9
print(f'A Temperatura {valor_fahrenheit} Fº(Fahrenheit) é igual a : {valor_celsius:.2f} Cº(Celsius)')

