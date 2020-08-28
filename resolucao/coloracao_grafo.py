colorir_cor_disponivel(vertice):
    # captura todos os vizinhos de vertice
    # verifica suas cores e descarta-as
    # colore vertice com alguma cor disponível


fila = [vertice_inicial]
colorido[vertice_inicial] = True

while fila:
    # remove o primeiro da fila
    vertice_atual = fila.pop(0)    

    # pega todos os vizinhos desse vertice
    # verifica se ele ja foi colorido
    for i in grafo[vertice_atual]: 
        if colorido[i] == False: 
            fila.append(i)
            colorir_cor_disponivel(colorido[i])
