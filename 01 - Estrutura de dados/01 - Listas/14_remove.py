# O método remove() é um método de listas que remove a primeira ocorrência de um elemento na lista.
# Se o elemento não estiver presente na lista, o método remove() levanta um ValueError.

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]
