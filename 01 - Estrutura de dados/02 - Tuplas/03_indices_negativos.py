# Índices negativos em tuplas. Assim como as listas, as tuplas também suportam índices negativos. 
# O índice -1 se refere ao último elemento da tupla, o índice -2 se refere ao penúltimo elemento, e assim por diante. 
# Isso é útil quando queremos acessar os elementos a partir do final da tupla, sem precisar conhecer o tamanho da tupla.    

frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

print(frutas[-1])  # pera
print(frutas[-3])  # laranja
