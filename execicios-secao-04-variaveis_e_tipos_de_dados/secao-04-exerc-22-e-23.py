"""
Exercicios de fixação
"""
# 22-23 - kilos para libras

convercao = int(input("Selecione a converção desejada \n0 -> Metros para Jardas\n 1 -> Jardas para Metros "))

if convercao == 0:
    medida1 = "Jardas"
    medida2 = "Metros"
    valor_1 = float(input(f"Digite o Valor em {medida1}"))
    convert = 0.91 * valor_1
elif convercao == 1:
    medida1 = "Metros"
    medida2 = "Jardas"
    valor_1 = float(input(f"Digite o Valor em {medida1}"))
    convert = valor_1 / 0.91

print(f'O valor de {valor_1} {medida1} é igual a {convert:.3f} {medida2}')
