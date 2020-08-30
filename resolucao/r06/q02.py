
# Python code to demonstrate working of  
# nlargest() and nsmallest() 
import heapq 
  
lista = [6, 7, 9, 4, 3, 5, 8, 10, 1] 
maiores = heapq.heapify([])
menores = heapq.heapify([])

n_iteracao = 1

# para cada item que for adicionado,
# verifique qual o numero da iteracao
for item_lista in lista:
    #iteracao impar
    if(n_iteracao % 2 == 1):
        pass


# using heapify() to convert list into heap 
#heapq.heapify(li1) 
  
# using nlargest to print 3 largest numbers 
# prints 10, 9 and 8 
#print("The 3 largest numbers in list are : ",end="") 
#print(heapq.nlargest(1, li1)) 
  
# using nsmallest to print 3 smallest numbers 
# prints 1, 3 and 4 
#print("The 3 smallest numbers in list are : ",end="") 
#print(heapq.nsmallest(1, li1)) 

