# A classe str é a classe de string do Python. Ela tem muitos métodos úteis para manipular strings.
# Alguns dos métodos mais comuns são:

nome = "gUIlherME"

print(nome.upper()) # Deixa todas as letras maiúsculas
print(nome.lower()) # Deixa todas as letras minúsculas
print(nome.title()) # Deixa a primeira let  ra maiúscula e o restante minúscula

texto = "  Olá mundo!    " # O método strip() remove os espaços em branco do início e do final da string. O método rstrip() remove os espaços em branco do final da string. O método lstrip() remove os espaços em branco do início da string.

print(texto + ".") # Imprime a string original com um ponto no final. O [+ "."] É UMA CONCATENAÇÃO DE STRINGS, OU SEJA, JUNTA DUAS STRINGS EM UMA SÓ. O PONTO É ADICIONADO PARA MOSTRAR ONDE TERMINA A STRING ORIGINAL, POIS ELA TEM ESPAÇOS EM BRANCO NO INÍCIO E NO FINAL.
print(texto.strip() + ".") # Imprime a string sem os espaços em branco do início e do final, com um ponto no final
print(texto.rstrip() + ".") # Imprime a string sem os espaços em branco do final, com um ponto no final
print(texto.lstrip() + ".") # Imprime a string sem os espaços em branco do início, com um ponto no final

menu = "Python" # O método center() centraliza a string em um campo de largura especificada. O método join() junta os elementos de uma lista em uma string, usando um separador especificado.

print("####" + menu + "####") # Imprime a string com quatro caracteres "#" antes e depois dela
print(menu.center(14)) # Imprime a string centralizada em um campo de largura 14, com espaços em branco preenchendo os lados
print(menu.center(14, "#")) # Imprime a string centralizada em um campo de largura 14, com caracteres "#" preenchendo os lados
print("-".join(menu)) # Imprime a string com cada caractere separado por um hífen
