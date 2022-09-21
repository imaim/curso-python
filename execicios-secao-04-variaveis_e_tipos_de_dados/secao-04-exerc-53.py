"""
Exercicios de fixação
"""
# 51


comprimento = float(input("Digite o comprimento do terreno em metros: "))
largura = float(input("Digite o largura do terreno em metros: "))
preco_tela = float(input("Digite o preço por metro da tela: "))
resultado = (comprimento * 2 + largura * 2) * preco_tela
print(f'O valor a ser pago por {comprimento * 2 + largura * 2} m de comprimento total é de R$: {resultado}')
