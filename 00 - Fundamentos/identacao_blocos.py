 # a identação em Python é fundamental para definir os blocos de código.
 # Ela indica quais linhas de código pertencem a um determinado bloco, como o corpo de uma função ou um bloco condicional. 
 # A falta de identação ou a identação incorreta pode levar a erros de sintaxe ou a comportamentos inesperados.   

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)
