"""
Recebendo dados do Usuario
# input - entrada
"""

# Entrada de dados
# print("Qual o seu nome ?")
mensagem = "Qual seu nome ?"
nome = input(f'{mensagem}')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)
# Exemplo de print moderno 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))
print(f'Seja bem-vindo(a) {nome}')

# print("Qual a sua idade ?")
idade = int(input("Qual a sua idade ?"))
# Processamento

# Saida
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))
# Exemplo de print moderno 3.x
# print('A {0} tem {1} anos'.format(nome, idade))
# Exemplo de print melhor , 3.7
print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2022 - int(idade)}')
