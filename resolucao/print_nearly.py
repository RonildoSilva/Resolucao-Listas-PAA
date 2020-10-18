lista_palavras = ['abajur','vidracaria','panqueca','cama', 'pá']
W = 10
i = 0; n = len(lista_palavras)
solucao = list()
pivo = 0

while(i < n):
    j = i + 1
    tam_j = len(lista_palavras[j])
    tam_i = len(lista_palavras[i])
    tam_linha = tam_i

    while(j < n and (tam_linha + tam_j + (j - i - 1)) < W ):
        tam_linha = tam_linha + tam_j
        j = j + 1

    diferenca = W - tam_linha
    numero_palavras = j - i

    solucao.append(numero_palavras)

    i = j

for s in solucao:
    print(lista_palavras[:s])
    for i in range(s):
        lista_palavras.pop(i)