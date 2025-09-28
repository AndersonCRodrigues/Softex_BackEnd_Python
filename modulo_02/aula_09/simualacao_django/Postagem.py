from .Model import Model
from .Usuarios import Usuario


class Postagem(Model):
    """
    Modelo de Postagem.
    Demonstra a composição, pois "tem um" objeto Usuario.
    """

    def __init__(self, id: int, titulo: str, conteudo: str, autor: Usuario):
        super().__init__(id)
        self.titulo: str = titulo
        self.conteudo: str = conteudo
        self.autor: Usuario = autor  # Composição: a Postagem tem um objeto Usuario

    def __str__(self) -> str:
        return (
            f"Postagem(id={self.id}, titulo='{self.titulo}', "
            f"autor='{self.autor.nome}')"
        )
