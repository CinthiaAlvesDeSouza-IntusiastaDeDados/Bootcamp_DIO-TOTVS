# O método sort() é um método de listas que ordena os elementos da lista in-place, ou seja, modifica a própria lista.
# O método sort() pode receber dois argumentos opcionais: reverse e key.
# O argumento reverse é um booleano que indica se a ordenação deve ser feita em ordem decrescente. 
# - O valor padrão é False, ou seja, a ordenação é feita em ordem crescente.
# O argumento key é uma função que recebe um elemento da lista e retorna um valor que será usado para comparar os elementos da lista.
# - O valor padrão é None, ou seja, os elementos da lista são comparados diretamente. 

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
