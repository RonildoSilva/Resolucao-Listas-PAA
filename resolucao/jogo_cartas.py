# pre-condicoes: lista com elementos, chave de busca
# pos-condiceos: indice do item encontrado ou -1, caso contrario
def busca_binaria(lista, chave):

    # indices da lista
    inicio = 0
    fim = len(lista) - 1
    meio = 0
  
    while inicio <= fim: 
        meio = (fim + inicio) // 2

        if lista[meio] < chave: 
            inicio = meio + 1
        elif lista[meio] > chave: 
            fim = meio - 1
        else: 
            return meio

    return -1

# pre-condicoes: A, lista com as cartas de ataque
#                DW, tupla valor de defesa d, peso w
# pos-condicoes: pontos: pontuacao máxima
def jogo_cartas(A, D, W):

    pontos = 0
    for i in range(len(A)):
        a = A[i]
        d = D[i]
        w = W[i]

        # se a é maior que o ultimo elemento de DW
        # então se deve usar o menor elemento d para
        # evitar o desperdicio de cartas maiores
        if(a > D[len(D)-1]):
            # atualizacao dos valores ja associados
            A[i] = -1; D[i] = -1; W[i] = -1
        # pergar o maior w onde d >= a
        else:
            indice = busca_binaria(D, A[i])
            # encontra pela busca
            if(indice == -1):
                pontos = pontos + W[indice]
                # atualizacao dos valores ja associados
                A[i] = -1; D[i] = -1; W[i] = -1
            # se nao encontra pela busca, apenas adicione
            # os demais valores de w, pois faz parte da solucao
            # otima
            else:
                pontos = pontos + W[i]
                # atualizacao dos valores ja associados
                A[i] = -1; D[i] = -1; W[i] = -1

    return pontos
    
        
A = [9,6,6,5,4,2,1]
D = [2,3,6,7,7,7,7]
W = [1,5,2,7,5,6,2]

#A.sort(reverse=True)

jogo_cartas(A,D,W)

