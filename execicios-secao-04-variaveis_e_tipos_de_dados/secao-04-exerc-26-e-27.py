"""
Exercicios de fixação
"""
# 26-27 -

convercao = int(input("Selecione a converção desejada \n0 -> M² para Hectares\n 1 -> Hectares para Metros M² "))

if convercao == 0:
    medida1 = "Hectares"
    medida2 = "M²"
    valor_1 = float(input(f"Digite o Valor em {medida1}"))
    convert = 10000 * valor_1
elif convercao == 1:
    medida1 = "M²"
    medida2 = "Hectares"
    valor_1 = float(input(f"Digite o Valor em {medida1}"))
    convert = valor_1 * 0.0001

print(f'O valor de {valor_1} {medida1} é igual a {convert:.3f} {medida2}')
