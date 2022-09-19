"""
Exercicios de fixação
"""
# 20-21 - kilos para libras

convercao = int(input("Selecione a converção desejada \n0 -> Kilos para Libras\n 1 -> Libras para Kilos "))

if convercao == 0:
    medida1 = "Kilogramas"
    medida2 = "Libras"
    valor_1 = float(input(f"Digite o Valor {medida1}"))
    convert = valor_1 / 0.45
elif convercao == 1:
    medida1 = "Libras"
    medida2 = "Kilogramas"
    valor_1 = float(input(f"Digite o Valor {medida1}"))
    convert = valor_1 * 0.45

print(f'O valor de {valor_1} {medida1} é igual a {convert} {medida2}')
