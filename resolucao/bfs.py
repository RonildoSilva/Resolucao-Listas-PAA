grafo = {
  0 : [1, 2],
  1 : [3],
  2 : [4, 5],
  3 : [1, 2, 6],
  4 : [6],
  5 : [3],
  6 : [4, 5]
}

def bfs(visitado, grafo, vertice):
  visitado.append(vertice)
  fila.append(vertice)
  resultado  = []

  while fila:
    s = fila.pop(0)
    resultado.append(s)

    for vizinhos in grafo[s]:
      if vizinhos not in visitado:
        visitado.append(vizinhos)
        fila.append(vizinhos)
  
  return resultado

values = []

k = int(input())

for _ in range(k):
    visitado = []
    fila = []

    line = input()

    if(len(line) == 1):
      x = int(line.split()[0])
      busca = bfs(visitado, grafo, 1) # 0 = S
      
      if (x in busca): # 0 = S
        print(busca.index(x))
      else:
        print('INF')

    elif(len(line) == 3):
      x = int(line.split()[0])
      y = int(line.split()[1])

      grafo[x].append(y)
    else:
      pass    

"""
busca = bfs(visitado, grafo, 1)
print(busca)
print(6 in busca)
print(busca.index(6))
"""

print(grafo)