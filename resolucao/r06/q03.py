"""
Entrada
3 5
C 1 2
F 1 2
C 1 2
F 1 3
C 1 3

Saída
N
S
S
"""

bancoA = {1}
bancoB = {2}
bancoC = {3}
bancoD = {4}
bancoE = {5}

operacoes = [
 ('C', bancoA, bancoB),
 ('F', bancoA, bancoB),
 ('C', bancoA, bancoB),
 ('F', bancoA, bancoC),
 ('C', bancoA, bancoC)
]

for op in operacoes:
    if(op[0] == 'C'):
        if(op[1] == op[2]):
            print('S')
        else:
            print('N')
    else:
        op[1].update(op[2])
        op[2].update(op[1])