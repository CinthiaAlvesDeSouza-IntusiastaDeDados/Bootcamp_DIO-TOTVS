# Fatiamento de tuplas. O fatiamento é uma técnica que permite acessar uma parte de uma tupla:
# - criando uma nova tupla com os elementos selecionados. 
# O fatiamento é feito utilizando a sintaxe [início:fim:passo],
# - onde início é o índice do primeiro elemento a ser incluído na nova tupla, 
# - fim é o índice do primeiro elemento a ser excluído da nova tupla, 
# - e passo é o intervalo entre os elementos selecionados. 
# Se início for omitido, o fatiamento começará do início da tupla.
# - Se fim for omitido, o fatiamento continuará até o final da tupla.
# - Se passo for omitido, o fatiamento selecionará todos os elementos entre início e fim.

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")
