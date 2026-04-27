# O método extend() é um método de listas que permite adicionar os elementos de uma lista a outra lista.
# O método extend() recebe um iterável como argumento e adiciona cada elemento do iterável à lista original. 
# O método extend() é diferente do método append(), que adiciona um único elemento. 

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
