"""
Exercicios de fixação
"""
# 36
fromimport math

valor1 = int(input("Digite o primeiro cateto do triangulo: "))
valor2 = int(input("Digite o segundo cateto do triangulo: "))
hipot = math.pow((valor1 ** 2 + valor2 ** 2))

print(f'A Hipotenusa do Triangulo é {hipot}')
