"""
PEP8 - Python Enchancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever codicos Python de forma Pythônicas.

[1] - utilize Camel Case para nomes de classe

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes minúsculo, separados por underline para funções e variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços em identação!

    if 'a' in 'banana':
        print('tem')

[4] - Linhas em Branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;
# Errado

import sys, os

# Import certo

import sys
import os

# Não há problemas em utilizar

from types import StringType, ListType

# Caso tenha muintos import de um mesmo pacote, recomenda-se fazer:

from type import (
    StringType,
    ListType,
    SetTye,
    OutroType
)

# Imports devem ser colocados no topo do arquivo,
# logo depois de quaisquer comentários ou docstrings e antes de constantes ou variáveis.

[6] - Espaços em expressões e insstuções
# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# faça:

funcao(algo[1], {outro: 2})

# nao faça:

algo (1)

#faça:

algo(1)

#nao faça:

dict ['chave'] = lista ['indice']

# faça:

dict['chave'] = lista['indice']

# nao faça
x     = 3
y     = 4
varivavel_longa = 3

# faça
x = 3
y = 4
varivavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""


import this
