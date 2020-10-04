# pre-condicoes: A, lista com as cartas de ataque
#                DW, tupla valor de defesa d, peso w
# pos-condicoes: pontos: pontuacao máxima

def jogo_cartas(A, DW):
    
    # estrutra i:(a,d,w)
    a_dict = dict()
    d_dict = dict()
    w_dict = dict()

    #A.sort(reverse=True)
    A.sort()
    DW.sort()

    for i in range(len(A)):
        a = A[i]
        d = DW[i][0]
        w = DW[i][1]

        a_dict.update({i: a})
        d_dict.update({i: d})
        w_dict.update({i: w})

    print(a_dict, d_dict, w_dict)

    # se [a] > ultimo elemento [d]
    #   associe o primeiro elemendo [d] disponivel a [a]

        #pontos = pontos + w
        #d = {i: (a,d,w)}
        #associacoes.update(d)
        
        # pega o maior [w] que tenha um [d] >= [a]
        
        #d = {i: (a,d,w)}
        #associacoes.update(d)
        

    # -1 para os que ja foram utilizados            

A = [4,6,2,7]
DW = [(6,1),(2,5),(7,2),(3,7)]


print(jogo_cartas(A, DW))
