# Fatiamaento de listas é uma técnica que permite extrair uma parte de uma lista, criando uma nova lista com os elementos selecionados. 
# O fatiamento é feito usando a sintaxe de colchetes [] e os índices de início, fim e passo.
# O índice de início é o índice do primeiro elemento a ser incluído na nova lista.
# O índice de fim é o índice do primeiro elemento a ser excluído da nova lista.
# Podemos ainda informar quantas posições o cursor deve "pular" no acesso.
# O índice de passo é a quantidade de elementos a serem pulados entre os elementos selecionados.

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
