class Filme:
    def __init__(self, titulo: str, diretor: str, ano: int):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        # "Filme: 'De Volta para o Futuro' (1985) - Diretor: Robert Zemeckis".
        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"


filme1 = Filme("Titanic", "Anderson", 1999)
print(filme1)
