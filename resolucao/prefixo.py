# pre-condicao:	listaA e listaB, listaA = um possível sub conjunto de listaB
# pos-condicao: tamanho da sequencia
#               lista dos indices da listaB a serem removidos
 
def prefixo_subsequencia(listaA, listaB):
    # variavel iterativa
    tamanho_sequencia = 0

    # armazenagem dos indices a serem removidos
    lista_indices_remocao = list()
  
    # para cada item na listaB (lista maior ou igual a listaA)
    for indice in range(len(listaB)) : 

        # verifica se o contador tem o mesmo
        # tamanho da listaA (lista menor ou igual listaB)
        # se tiver, não é mais necessário verificar
        # pois a lista já foi totalmente verificada
        if (tamanho_sequencia == len(listaA)): 
            break
  		
		# para cada ocorrencia do mesmo termo em 
        # listaA e listaB, incremente a quantidade
        # correspondente ao tamanho da sequencia
        if (listaB[indice] == listaA[tamanho_sequencia]) : 
            tamanho_sequencia = tamanho_sequencia + 1
        # adiciona a lista o indice que deve ser removido de listaB
        else:
            lista_indices_remocao.append(indice)
              
  
    return tamanho_sequencia , lista_indices_remocao
  
  
# Driver Code 
S = "digger"
T = "biggerdiaggram"
  
print(prefixo_subsequencia(S, T)) 
  
  
# This code is contributed 
# by Nikita Tiwari. 
