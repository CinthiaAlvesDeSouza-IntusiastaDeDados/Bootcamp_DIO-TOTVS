# Filtrar lista. A compreensão de lsita oferece uma sinatxe mais curta quando você deseja:
# - criar uma nova lista com base em uma sequência ou iterável existente (filtro),
# ou apenas incluindo elementos que atendam a uma condição específica (modificar valores).

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
