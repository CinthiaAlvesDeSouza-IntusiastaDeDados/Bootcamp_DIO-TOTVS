# Contando elementos em tuplas. Assim como as listas, as tuplas também possuem o método count(),
# - que permite contar quantas vezes um determinado elemento aparece na tupla.  

cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
