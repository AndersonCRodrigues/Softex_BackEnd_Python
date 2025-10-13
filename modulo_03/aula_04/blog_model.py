"""
Crie a class BlogModel seguindo o exemplo da UserModel;
BlogModel deve ter os atributos:
 - conn do tipo DatabaseConnection
 - criar a tabela quando instanciado

tabela blogs:
 - id;
 - titulo;
 - conteudo;
 - data_criacao;
 - data_atualizacao;
 - id_user (chave estrangeira referente a tabela usuarios);

Faça um CRUD para:
- criar postagem
- ler todas as postagens
- ler postagens pelo id
- ler postagens pelo id_user
- atualizar postam (pelo id da postagem)
- deletar postagem (pedo id da postagem)

**Consulte o UserModel para se guiar
"""