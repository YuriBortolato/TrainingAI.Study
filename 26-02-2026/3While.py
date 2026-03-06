#**Loop de Repetição - While**

'''
    A estrutura de controle **while** é utilizada para criar loops enquanto 
    uma condição específica permanecer verdadeira.

    O código dentro do bloco é repetido iterativamente até quando seja avaliada como falsa, 
    permitindo a execução repetidamente enquanto a condição é atendida.
'''

#Exemplos

#while simples
i = 0
while i < 5:
  print(i)
  i += 1

i = int(input('Informe um valor inteiro para i:'))

#while com else
while i < 3:
  print(i)
  i += 1
else:
  print(i)
