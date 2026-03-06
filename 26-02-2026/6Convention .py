#**Convenção - Modificadores de Acesso**

'''
    **Não existem** modificadores de acesso como em outras linguagens. 
    O Python utiliza convenções para determinar o nível de acesso de uma variável ou método.



    #* _nome -> variáveis e métodos que começam com **um** *underline* são considerados **privados**
    #* __senha -> variáveis e métodos que começam com **dois** *underlines* são considerados **protegidos**
    #* idade -> variáveis e métodos que **não começam** com nenhum dos dois são considerados **público**
'''

#Orientação a Objetos - Classes

#exemplo de uma classe em python
class Pessoa:

  #essa função define o metodo construtor, OBRIGATÓRIAMENTE o nome deve ser __init__
  #self -> palavra reservada que indica a própria instância, semelhante ao this do C#/Java
  #OBRIGATÓRIAMENTE o self sempre será o primeiro parâmetro
  #os demais parâmetros são os que serão utilizados para inciar o valor nos atributos
  def __init__(self, documento, nome):
    #os atributos de uma classe no Python sçao definidos no momento em que são declarados
    #neste ponto exato do código a classe não possui nenhum atributo
    self.__documento = documento #atributo privado segundo a convenção
    self.__nome = nome
    #neste ponto exato do código possui 2 atributos (__documento e __nome)

  #segundo a convenção os dois métodos abaixo são publicos
  def get_documento(self):
    return self.__documento

  def get_nome(self):
    return self.__nome

#xemplo instanciando classe
pessoa_um = Pessoa(documento="000.000.000-45", nome="PESSOA TESTE")
print(pessoa_um.get_documento() + " " + pessoa_um.get_nome())

