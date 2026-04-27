# Iterando sobre tuplas. Assim como as listas, as tuplas também são iteráveis, 
# - ou seja, podemos percorrer seus elementos utilizando um loop for.
# Durante a iteração, cada elemento da tupla é atribuído a uma variável temporária, 
# - que pode ser utilizada dentro do bloco do loop para realizar operações ou exibir os elementos.

carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
