# Declarando tuplas. Tuplas são estruturas de dados muito parecidas com as listas.
# A diferença é que as tuplas são imutáveis, ou seja, não podem ser alteradas após serem criadas. 
#  As tuplas são declaradas utilizando parênteses () e os elementos são separados por vírgulas. 
# Se a tupla tiver apenas um elemento, é necessário adicionar uma vírgula após o elemento para que seja reconhecida como uma tupla.

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
