from services import UsuarioService, PostagemService
from Usuarios import Usuario
from Postagem import Postagem
from db import db_usuarios, db_postagens

if __name__ == "__main__":
    # Instanciando (criando objetos) os serviços.
    usuario_service: UsuarioService = UsuarioService()
    postagem_service: PostagemService = PostagemService()

    print("--- 1. Criando usuários ---")
    user1: Usuario = usuario_service.create_usuario("Alice", "alice@email.com")
    user2: Usuario = usuario_service.create_usuario("Bob", "bob@email.com")
    print(user1)
    print(user2)
    print("-" * 25)

    print("--- 2. Acessando atributos e usando getters/setters ---")
    print(f"Nome do usuário 1: {user1.nome}")
    print(f"ID do usuário 1: {user1.id}")
    print(f"Email do usuário 1: {user1.email}")

    user1.email = "novo_email.com"

    user1.email = "alice.nova@email.com"
    print(f"Novo email do usuário 1: {user1.email}")
    print("-" * 25)

    print("--- 3. Criando postagens (demonstrando Composição) ---")
    post1: Postagem = postagem_service.create_postagem(
        titulo="Primeira Postagem",
        conteudo="Conteúdo da primeira postagem...",
        autor=user1,
    )
    post2: Postagem = postagem_service.create_postagem(
        titulo="Uma postagem do Bob",
        conteudo="Olá, este é o Bob!",
        autor=user2,
    )
    print(post1)
    print(post2)
    print("-" * 25)

    print("--- 4. Buscando dados do 'DB' ---")
    postagem_buscada: Postagem | None = postagem_service.get_postagem(
        id_=post1.id,
    )
    if postagem_buscada:
        print(
            f"Postagem encontrada: '{postagem_buscada.titulo}'"
            f"do autor {postagem_buscada.autor.nome}"
        )

    print(f"Número total de usuários: {len(db_usuarios)}")
    print(f"Número total de postagens: {len(db_postagens)}")
