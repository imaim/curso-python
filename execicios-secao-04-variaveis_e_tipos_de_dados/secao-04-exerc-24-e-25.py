"""
Exercicios de fixação
"""
# 24-25 - kilos para libras

convercao = int(input("Selecione a converção desejada \n0 -> M² para Acres\n 1 -> Acres para Metros M² "))

if convercao == 0:
    medida1 = "Acres"
    medida2 = "M²"
    valor_1 = float(input(f"Digite o Valor em {medida1}"))
    convert = 04048.58 * valor_1
elif convercao == 1:
    medida1 = "M²"
    medida2 = "Acres"
    valor_1 = float(input(f"Digite o Valor em {medida1}"))
    convert = valor_1 * 0.000247

print(f'O valor de {valor_1} {medida1} é igual a {convert:.3f} {medida2}')
