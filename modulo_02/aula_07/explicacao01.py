class User:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome
    
animal =  User("Rex")
print(animal.nome)
print(animal)