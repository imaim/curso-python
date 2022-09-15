"""
Escopo de Varaveis

Dois casos de Escopo
1 - Variaveis globais:
    - Variáveis globais são reconhecidas, seu escopo compreende, todo o programa.
2 - Variaveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está
    limitado ao bloco onde foi declarada.

Para declarar variais em python fazemos:

nome_da_variavel = valor_da_variavel
ex:
    numero = 42

Python é uma linguagem de tipagem dinámica. Isso significa que ao declarar uma veriavel,
nos não colocamos o tipo dela.
Este tipo é inferido ao atribuirmos o valor à mesma.
Exemplo em C:
int numero = 42;
"""


# Variavel Global
numero = 42
print(numero)
print(type(numero))

# Variavel local

numero = 2
if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)