# produtos como um hash
# onde a chave é o nome do produto
# e o valor, o preco do produto
# com (m) produtos
produtos = {
    "pão": 2.39, "leite": 5.29,
    "sabonete": 1.09, "sabão em pó": 9.99
}

# lista de compras representada por 
# uma lista de items de tamanho (n)
lista_compras = ["leite", "sabonete", "sabonete"]

soma = 0
# laco de repeticao da ordem 
# do tamanho da lista O(n)
for item in lista_compras:
    # para cada iteracao sobre a lista, 
    # adicione a variavel soma, o preco do 
    # produto obtido pela consulta no 
    # hash de tamanho (m)
    soma = soma + produtos.get(item)

# retorne a soma
return soma


