"""
Estruturas Logicas:
AND OR NOT IS

Regras de funcionamento:
and > ambos os valores precisam ser True
or > ao menos um dos valores precisa ser True
not > o valor do booleano é invertido, ou seja, se for True, vira False ou vice e versa

exemplos :
if ativo or logado:
    print(f'Bem-vindo usuário!')
else:
    print(f'Você precisa ativar sua conta. Por favor, cheque seu e-mail.')

if not ativo:
    print(f'Você precisa ativar sua conta. Por favor, cheque seu e-mail.')
else:
    print(f'Bem-vindo usuário!')

if ativo:
    print(f'Você precisa ativar sua conta. Por favor, cheque seu e-mail.')
else:
    print(f'Bem-vindo usuário!')
"""


ativo = True
logado = True

if ativo:
    print(f'Você precisa ativar sua conta. Por favor, cheque seu e-mail.')
else:
    print(f'Bem-vindo usuário!')

