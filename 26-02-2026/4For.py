#**Loop de Repetição - For**
'''
    O *loop for* é usado para iterar sobre uma sequência (como uma lista, tupla ou string) 
    ou qualquer outro objeto que seja iteravel. Ele simplificar a iteração em elementos, 
    percorrendo a sequência e executando um bloco de código para cada item, proporcionando 
    uma forma eficiente de processar coleções.
'''

#Exemplo

#for simples
nome = input("Digite seu nome: ")
for letra in nome:
  print(letra)

numeros = [1, 3, 5, 7, 9]
for numero in numeros:
  print(numero)

#for com reversed
for letra in reversed(nome): #está função recebe uma string e a retorna invertida
  print(letra)

#for com reverse
lista = [1, True, "Teste", 0.99]
lista.reverse()

for item in lista:
  print(item)


