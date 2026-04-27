# O método sorted() é uma função embutida em Python que retorna uma nova lista ordenada a partir de um iterável.
# O método sorted() pode receber dois argumentos opcionais: reverse e key.
# O argumento reverse é um booleano que indica se a ordenação deve ser feita em ordem decrescente. 
# - O valor padrão é False, ou seja, a ordenação é feita em ordem crescente.
# O argumento key é uma função que recebe um elemento do iterável e retorna um valor que será usado para comparar os elementos do iterável.
# - O valor padrão é None, ou seja, os elementos do iterável são comparados diretamente.    

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
