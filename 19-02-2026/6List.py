#Estrutura de Dados

#Lista
'''
*É uma estrutura de dados flexível que armazena elementos mutáveis e ordenaveis, 
é definida por colchetes []. Suporta diversos tipos de dados, permitindo operações de adição, 
remoção e indexação*
'''

#declaração de uma lista vazia
variavel_lista_vazia = []

#declaração de uma lista com elementos do mesmo tipo
variavel_lista_mesmo_tipo = ["Amazon", "Google", "Facebook", "Uber"]

#declaração de uma lista com elementos de tipos diferentes
variavel_lista_tipos_diferentes = ["Mercado Pago", 1, 3.14, True]

#adicionando elementos em uma lista
variavel_elementos = []
print(variavel_elementos)

variavel_elementos.append("IOB")
print(variavel_elementos)

#editando um elemento da lista
variavel_elementos[0] = "IOB Auditor"
variavel_elementos.append("IOB Auditor")
print(variavel_elementos)

#remover um elemento da lista
variavel_elementos.remove("IOB Auditor")
print(variavel_elementos)

#trocando o tipo de dado de uma variavel
variavel_elementos = None
variavel_elementos = 3.14
print(variavel_elementos)