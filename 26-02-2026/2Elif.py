#**Controle de Fluxo**

'''
    A estrutura condicional *if* permite a execução condicional de 
    blocos de código com base em uma expressão booleana.

    Se a condição for verdadeira, o bloco associado é executado; 
    caso contrário, o fluxo do programa pode seguir caminhos alternativos com *elif* ou *else*
'''
#Exemplos

#input retorna sempre uma string
#int converte a string em um inteiro
numero = int(input("Digite um número inteiro válido: "))

#if simples
if numero % 2 == 0:
  #str função de conversão de int para string
  print("O número " + str(numero) + " é par.")

#if & else
if numero % 2 == 0:
  print("O número é par.")
else:
  print("O número é ímpar.")


idade = 32

#if & elif & else
if idade < 18:
  print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
  print("Você é adulto.")
else:
  print("Você é idoso.")
