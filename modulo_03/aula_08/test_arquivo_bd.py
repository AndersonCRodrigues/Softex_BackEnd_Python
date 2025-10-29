import pytest
from arquivo_db import ConexaoDB, GerenciadorTarefas


# FIXTURE 1: Cria e Limpa a Dependência
@pytest.fixture
def conexao_db_limpa():
    """Cria um DB temporário (:memory:) e garante o fechamento (Teardown)."""
    # SETUP
    conexao = ConexaoDB(db_path=":memory:")

    yield conexao  # Entrega o objeto de conexão

    # TEARDOWN: Código executado após o teste
    conexao.fechar()


# FIXTURE 2: Monta a Classe a Ser Testada
@pytest.fixture
def gerenciador_tarefas_isolado(conexao_db_limpa):
    """Monta o GerenciadorTarefas, INJETANDO a ConexaoDB limpa."""
    # Ocorre a Composição
    return GerenciadorTarefas(db_conn=conexao_db_limpa)


def test_contagem_inicia_em_zero(gerenciador_tarefas_isolado):
    """Verifica o estado inicial (DB limpo)."""
    assert gerenciador_tarefas_isolado.contar_tarefas() == 0


def test_adicionar_tarefa_incrementa_contador(gerenciador_tarefas_isolado):
    """Verifica a adição de dados no DB isolado."""
    gerenciador_tarefas_isolado.adicionar_tarefa("Revisar Fixtures")
    gerenciador_tarefas_isolado.adicionar_tarefa("Nova Tarefa")
    assert gerenciador_tarefas_isolado.contar_tarefas() == 2
