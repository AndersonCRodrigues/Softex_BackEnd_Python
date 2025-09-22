"""
Objetivo: Criar uma classe com validações simples nos setters para tipo e valor. 
●  Requisitos: 
1.  Crie uma classe Pessoa com os atributos protegidos _nome e _idade. 
2.  Crie uma @property para nome. 
3.  Crie um @nome.setter que valide se o valor é uma string e não está vazio. 
4.  Crie uma @property para idade. 
5.  Crie um @idade.setter que valide se a idade é um número inteiro e positivo. 
6.  No __init__, use os setters para atribuir os valores iniciais (ex: self.nome = nome). 
7.  Instancie um objeto Pessoa com dados válidos e depois tente alterar nome para um 
valor vazio e idade para um valor negativo para testar as validações. 
 
"""

class Pessoa:
    def __init__(self, nome:str, idade:int):
        if nome and isinstance(nome, str):
            self._nome = nome
        else:
            self._nome = "Não definido"
        if idade > 0 and isinstance(idade, int):
            self._idade = idade
        else:
            self._idade = "Desconhecida"

    @property # me devolve o valor do atributo protegido
    def nome(self): # nome do getter
        return self._nome
    
    @nome.setter # pode alterar o valor do atributo protegido
    def nome(self, novo_nome: str): # nome do setter == nome do getter
        # isisntance verifica se o primeiro parametro é do tipo do segundo
        if isinstance(novo_nome, str) and novo_nome:
            self._nome = novo_nome
        else:
            print("Erro! O novo nome deve ser uma string não vazia")

    @property
    def idade(self):
        return self._idade


    @idade.setter
    def idade(self, nova_idade:int):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Erro! Nova idade deve ser um inteiro positivo!")

nova_pessoa = Pessoa("", -42)
print(nova_pessoa.nome)
nova_pessoa.nome = "Pedro"
print(nova_pessoa.nome)
nova_pessoa.idade = 40
print(nova_pessoa.idade)
