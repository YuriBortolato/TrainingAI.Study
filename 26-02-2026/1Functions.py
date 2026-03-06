#**Functions**

'''
-   São blocos de código reutilizáveis definidos pela palavra reservada ou palavra chave **def**.

-   Permitem encapsular lógicas específicas, aceitar parãmetros e retornar valores.

-   Funções melhoram a modularidade, legibilidade do código e promovem a prática *DRY - Dont't Repeat Yourself*

-   Argumentos podem ser passados por posições ou nome, e funções podem ter valores de retorno opcionais.

'''

#exemplo de uma função em python
def minha_primeira_funcao(parametro_um):
  #corpo da função
  return "Olá " + parametro_um + "!"

#def -> palavra chave que indica o início da definição de uma função
#minha_primeira_funcao -> nome escolhido para a função (convenção snake_case)
#parametro_um -> é o argumento que a função recebe como parâmetro de entrada (opcional)
#: (dois pontos) -> indica  o fim da linha de definição de uma função e o inicio
#                   do corpo da função
#return -> palavra chave que indica o valor de retorno da função (opcional

minha_primeira_funcao(input("Digite seu nome: "))
