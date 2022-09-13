#!/usr/bin/env python

alunos = {
    "aluno": {"nome": "maria", "idade": 19, "nota": 6.2, "cor":["rosa","amarelo"] } , "turma" : "3b"
    }
for key in alunos.keys() :
    while True:
        if key == "aluno":
            print(alunos[key]["cor"][0])
            break
        else :
            print(alunos[key])
            

