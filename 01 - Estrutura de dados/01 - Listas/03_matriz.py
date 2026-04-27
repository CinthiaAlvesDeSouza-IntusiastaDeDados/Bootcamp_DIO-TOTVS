
# Listas podem armazenar todos os tipos de objetos, incluindo outras listas, formando assim uma estrutura de dados chamada matriz ou lista de listas.
# Com isso podemos criar estruturas bidimensionais (tabelas) ou até mesmo tridimensionais (cubos de dados).
# Para acessar os elementos de uma matriz, usamos dois índices: o primeiro índice para acessar a linha e o segundo índice para acessar a coluna.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
