from .Usuarios import Usuario
from .Postagem import Postagem
from .db import db_usuarios, db_postagens, gerar_id_aleatorio


class UsuarioService:
    """
    Serviço para gerenciar a lógica de usuários.
    Responsabilidade única de criar e buscar usuários.
    """

    def create_usuario(self, nome: str, email: str) -> Usuario:
        id_gerado: int = gerar_id_aleatorio(db_usuarios)
        usuario: Usuario = Usuario(id_gerado, nome, email)
        db_usuarios[id_gerado] = usuario
        return usuario

    def get_usuario(self, id_: int) -> Usuario | None:
        return db_usuarios.get(id_)


class PostagemService:
    """
    Serviço para gerenciar a lógica de postagens.
    """

    def create_postagem(
        self,
        titulo: str,
        conteudo: str,
        autor: Usuario,
    ) -> Postagem:
        id_gerado: int = gerar_id_aleatorio(db_postagens)
        postagem: Postagem = Postagem(id_gerado, titulo, conteudo, autor)
        db_postagens[id_gerado] = postagem
        return postagem

    def get_postagem(self, id_: int) -> Postagem | None:
        return db_postagens.get(id_)
