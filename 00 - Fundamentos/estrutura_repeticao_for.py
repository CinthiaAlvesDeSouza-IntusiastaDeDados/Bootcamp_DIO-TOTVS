# Estrutura de repetição for em Python é usada para iterar sobre uma sequência 
# (como uma lista, tupla, string ou range) e executar um bloco de código para cada item da sequência.
# A sintaxe básica é:

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
