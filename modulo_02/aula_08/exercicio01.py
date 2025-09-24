class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e curso {self.curso}")


pessoa = Pessoa("Luzia", 64)
estudante = Estudante("João", 33, "Gestão de Software")

lista_objetos:list[Pessoa] = [pessoa, estudante]

for objeto in lista_objetos:
    objeto.apresentar()