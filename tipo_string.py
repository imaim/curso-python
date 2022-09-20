"""
Tipo String

Em python, um dado é considerado do tipo String sempre que:
- Estiver entre àspas simples -> 'uma string', '1', '@', 'True', '43.3'
- Estiver entre àspas duplas -> "uma string", "1", "@", "True", "43.3"

print(f'{nome.upper()}') # tudo para maiúsculo
print(f'{nome.lower()}') # tudo para minúsculo
print(f'{nome.split()}') # transforma em uma lista de string, utilizando determinado separado (default e o " ")
    ex:
    nome = "geek University"
    print(f'{nome.split()}')
    result >>> ['geek', 'University']
    nome = "geek.University"
    print(f'{nome.split(".")[1]}')
    result >>> ['University']
print(f'{nome.[1]}') # Slice de string # posição 1 da string (começa sempre em 0)
print(f'{nome.[0:5]}') # exibe da posição 0 a posição 5 da string
print(f'{nome.[::-1]}') # percorre toda a string e exibe de forma invertida
print(f'{nome.replace("e", "i")}') # substitui todos o "e" por "i"
"""
# - Estiver entre àspas simples triplas e duplas triplas """uma string""", '''1''', '''@''', """True""", """43.3""""

nome = "Geek University"
print(f'{nome.replace("e", "i")}')
#
print(f'{nome[1]}')
# nome = "Imaim Vilela"
if type(nome) is str:
    print(f'A variável é uma {type(nome)}')

