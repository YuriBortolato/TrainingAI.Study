#**Tratamento de Exceção - try/excep/finally**

'''
-   O bloco *try* é utilizado para envolver o código que pode gerar uma exceção.

-   O bloco *except* permite tratar exceções específicas.

-   O bloco *finnaly* contém código que sempre será executado, 
    independentemente de ocorrer ou não uma exceção. Sendo útil para ações de limpeza.
'''

#Exemplo

def funcao_com_excecao():
  #exemplo de disparo de uma exceção
  raise Exception("Mensagem de erro é opcional") #raise -> é a palavra reservada para "estourar" uma exception

#exemplo manipulando a exception
try:
  funcao_com_excecao()
  print("Teste") #nunca será executada pois o metodo anterior a ela gera uma exceção
except Exception as e:
  print(e)
finally: #(opcional)
  print("log: bloco try/except/finally")

#exemplo ignorando o tratamento da exception
try:
  funcao_com_excecao()
  print("Teste") #nunca será executada pois o metodo anterior a ela gera uma exceção
except Exception as e:
  pass #pass -> ignora o tratamento
  print(e)
finally: #(opcional)
  print("log: bloco try/except/finally")
