#Outras funções em uma lista

"""
1. insert()- insere um elemento na lista em uma determinada posição
2. remove() - remove a primeira ocorrencia de um elemento na lista
3. pop() - remove e retorna o último elemento da lista (ou em uma determinada posição)
4. count() - retorna o número de ocorrências de um elemento na lista
5. index() - retorna a primeira posição de um elemento na lista
6. reverse() - inverte a ordem dos elementos da lista
7. sort() - ordena os elemtnos da lista (default ordem crescente)

"""

#Tuple
'''
A tuple é uma estrutura de dados imutável e ordenada, definada por **parênteses ()**. 
Igualmente a list, podem conter diferentes tipos de dados, mas sua imutabilidade oferece 
mais segurança contra alterações acidenteais.

'''

#declaração de uma tuple vazia
variavel_tuple_vazia = ()

#declaração de uma tuple com os elementos do mesmo tipo
variavel_tuple_elementos_mesmo_tipo = ("Netflix", "YouTube", "Naruto Project")

#declaração de uma tuple com elementos de tipos diferentes
variavel_tuple_elementos_de_tipos_diferentes = ("PicPay", 42, True)

#acessando o elemento de uma tuple
print(variavel_tuple_elementos_mesmo_tipo[2])