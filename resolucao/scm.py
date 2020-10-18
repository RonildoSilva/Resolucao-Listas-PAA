L = [1,5,2,5,-3,4,52,-23,45]
S = [0,0,0,0,0,0,0,0,0]
# array que armazena as substancias
A = [0,0,0,0,0,0,0,0,0]

# casos base
S[0] = L[0]
A[0] = L[0]

valor_maximo = S[0]
indice_inicio = 0
indice_fim = 0

# percurso da tabela
for i in range(1, len(L)):
    if(S[i-1] > 0):
        S[i] = S[i-1] + L[i]
        A[i] = A[i-1]
    else:
        S[i] = L[i]
        A[i] = i

    if(S[i] > valor_maximo):
        indice_inicio = A[i]
        indice_fim = i
        valor_maximo = S[i]

print(indice_inicio, indice_fim)
print(L[indice_inicio:indice_fim])