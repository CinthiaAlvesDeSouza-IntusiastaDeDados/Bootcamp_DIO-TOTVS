# A string é uma sequência de caracteres. Ela é imutável, ou seja, não pode ser alterada depois de criada. As strings podem ser criadas usando aspas simples ('), aspas duplas (") ou aspas triplas (''' ou """).
# As aspas triplas são usadas para criar strings multilinha, ou seja, strings que ocupam mais de uma linha. As strings podem ser formatadas usando o método format() ou f-strings. 
# O método format() permite inserir valores em uma string usando marcadores de posição, como {}.
#  As f-strings permitem inserir valores em uma string usando expressões entre chaves {}, precedidas pela letra f.

nome = "Cinthia"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)


print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)
