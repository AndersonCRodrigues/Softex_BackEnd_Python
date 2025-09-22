class User:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"seu nome é {self.nome}"
    
animal =  User("Rex")
print(animal.nome)
texto = animal
print(texto)