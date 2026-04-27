# a estrutura de repetição break em Python é usada para interromper a execução de um loop (for ou while),
# quando uma condição específica é atendida.  Quando o comando break é executado, 
# o loop é imediatamente encerrado e a execução do programa continua a partir da próxima linha de código após o loop.
# Isso é útil para sair de um loop quando um resultado desejado é alcançado ou quando uma condição de parada é satisfeita.
# Evitando a necessidade de verificar a condição em cada iteração do loop.

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
