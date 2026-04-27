# Matrizes utilizando tuplas. Uma matriz é uma estrutura de dados bidimensional:
# - ou seja, é uma coleção de elementos organizados em linhas e colunas.
# Em Python, podemos representar uma matriz utilizando tuplas de tuplas.
# - Cada tupla interna representa uma linha da matriz, e os elementos dentro dessas tuplas representam as colunas. 
# Para acessar um elemento da matriz, basta utilizar dois índices: 
# - o primeiro índice para a linha e o segundo índice para a coluna.

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
