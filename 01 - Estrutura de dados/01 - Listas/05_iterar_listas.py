# Iterar Listas, a forma mais comum para percorrer os dados de uma lista é usando um loop for. 
# O loop for permite iterar sobre os elementos da lista, executando um bloco de código para cada elemento.
# A função enumerate() é uma função embutida do Python que permite iterar sobre uma sequencia, como uma lista, e obter o índice e o valor de cada elemento ao mesmo tempo.

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
