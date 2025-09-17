class Cachorro:
    def __init__(self, nome: str, cor: str) -> None:
        self.nome = nome
        self.cor = cor

    def latir(self, fala: str) -> None:
        print(f"{self.nome} diz: {fala}!")

# cria um objeto do tipo class Cachorro
meu_cachorro = Cachorro("Rex", "preto")

# nome e cor são atributos (variaves) da class Cachorro
# por isso não são chamadas com parênteses: ()
print(meu_cachorro.nome)
print(meu_cachorro.cor)

# chama o método (função) latir passando parâmento
meu_cachorro.latir("Miau")
