class Filme:
    def __init__(self, titulo: str, diretor: str, ano: int):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        # "Filme: 'De Volta para o Futuro' (1985) - Diretor: Robert Zemeckis".
        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"


filme1 = Filme("De Volta para o Futuro", "Robert Zemeckis", 1985)
print(filme1)


bonus = 1.10
salario = 100
salario_com_bonus = salario * bonus
print(salario_com_bonus)
