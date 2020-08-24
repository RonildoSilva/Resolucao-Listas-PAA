
def busca_matriz_ordenada(M, key):

    col_index = -1

    # se a chave é menor que 
    # o menor elemento da matriz
    # retorne falso
    if(key < M[0][0]):
        return False

    # busca coluna
    for i in range(len(M[0])):
        # encontra coluna 
        if(key < M[0][i]):
            # captura coluna anterior onde
            # possivelmente esta a solucao
            col_index = i - 1

    # busca linha
    # para cada elemento da linha
    for j in range(len(M)):
        # verifique a existendia de um 
        # elemento da linha igual a chave
        if(key == M[j][col_index]):
            # se existe, retorne verdadeiro
            return True
    
    return False

M = [
    [10, 20, 30, 40, 50],
    [12, 22, 32, 42, 52],
    [14, 24, 34, 44, 54],
    [16, 26, 36, 46, 56]
    ]

key = 42

print(busca_matriz_ordenada(M, key))