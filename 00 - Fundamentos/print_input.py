input # Função de entrada built-in do Python, usada para ler dados do usuário.
output # Função de saída built-in do Python, geralmente usada para exibir informações para o usuário, como a função print() em Python.   
    
input("Informe o seu nome: ") # Solicita ao usuário que informe seu nome e armazena a entrada em uma variável.
print("Olá, " + nome + "!") # Exibe uma mensagem de saudação personalizada usando a variável que contém o nome do usuário.  

nome = input("Informe o seu nome: ") # Solicita ao usuário que informe seu nome e armazena a entrada em uma variável chamada 'nome'.
idade = input("Informe a sua idade: ") # Solicita ao usuário que informe sua idade e armazena a entrada em uma variável chamada 'idade'.

print(nome, idade) # Exibe o nome e a idade do usuário, separados por um espaço. O print() pode aceitar múltiplos argumentos e os separa por um espaço por padrão.  
print(nome, idade, end=" ...\n") # Exibe o nome e a idade do usuário, separados por um espaço, e termina a linha com " ..." seguido de uma nova linha. O argumento end é usado para especificar o que deve ser impresso no final da linha, em vez do comportamento padrão de adicionar uma nova linha.
print(nome, idade, sep=" - ") # Exibe o nome e a idade do usuário, separados por " - ". O argumento sep é usado para especificar o que deve ser impresso entre os argumentos, em vez do comportamento padrão de um espaço.  

print(nome, idade, sep=" - ", end=" ...\n") # Exibe o nome e a idade do usuário, separados por " - ", e termina a linha com " ..." seguido de uma nova linha. Combina os argumentos sep e end para personalizar tanto o separador entre os argumentos quanto o que é impresso no final da linha.    
print("Olá, " + nome + "!") # Exibe uma mensagem de saudação personalizada usando a variável 'nome' que contém o nome do usuário. A concatenação de strings é feita usando o operador + para combinar a string "Olá, " com o valor da variável 'nome' e a string "!".   

