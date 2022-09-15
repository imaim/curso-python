"""
Tipo Booleano

Algebra Booleana, criado por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Faso
OBS: Sempre com a primeira letra maiúscula
Errado:
    true, false
Certo:
    True, False

"""

ativo = True
print(ativo)

"""
Operações Basicas:
"""
# Negação (not):
"""
Fazendo a negação, se o valor for verdadeiro o resultado será falso,
 se falso o resultado será verdadeiro.
"""

print(not ativo)

logado = False

# Ou (or):
"""
E um operação binaria, precisa de dois valores onde ao menos 1 deve ser verdadeiro para o resultado ser verdadeiro
"""
print(ativo or logado)

# E (and):
"""
E uma operação binaria, ambos os valores devem ser verdadeiros para o resultado ser verdadeiro
"""
print(ativo or not logado)
