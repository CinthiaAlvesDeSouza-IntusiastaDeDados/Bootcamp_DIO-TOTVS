# Índice de elementos em tuplas. O método index() é utilizado para encontrar o índice da primeira ocorrência de um elemento em uma tupla.
# Ele recebe como argumento o elemento que queremos encontrar e retorna o índice correspondente.
# Se o elemento não estiver presente na tupla, o método index() lançará uma exceção ValueError. 
# O método index() é útil para verificar a posição de um elemento específico em uma tupla, 
# - especialmente quando precisamos acessar ou manipular elementos com base em sua posição.

linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
