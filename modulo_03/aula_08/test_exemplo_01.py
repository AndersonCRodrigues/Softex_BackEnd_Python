from exemplo_01 import (
    gerar_id_composto,
    jogar_dado_seis_lados,
    verificar_numero_secreto,
    func,
)
import pytest


def test_resultado_d_jogar_um_dado_seis_lados(mocker):
    resultados_random = [1, 2, 3]
    mocker.patch("exemplo_01.random.randint", side_effect=resultados_random)
    assert jogar_dado_seis_lados() == 1
    assert jogar_dado_seis_lados() == 2
    assert jogar_dado_seis_lados() == 3


@pytest.mark.parametrize(
    "mock_sequence, expected_id",
    [
        # Cenário 1: Sequência simples (Mock retorna [1, 1, 1, 1])
        ([1, 1, 1, 1], "1111"),
        # Cenário 2: Sequência complexa (Mock retorna [9, 8, 7, 6])
        ([9, 8, 7, 6], "9876"),
        # Cenário 3: Sequência alternada (Mock retorna [2, 5, 2, 5])
        ([2, 5, 2, 5], "2525"),
    ],
)
def test_gerar_id_composto_com_parametrizacao(
    mocker,
    mock_sequence,
    expected_id,
):
    """
    Roda o mesmo teste 3 vezes, injetando uma
    sequência diferente no Mock a cada rodada.
    """
    # 1. Cria o Mock AGORA, usando a sequência fornecida pelo parametrize
    mock_randint = mocker.Mock(side_effect=mock_sequence)
    # 2. Patch: Substitui a função real pelo mock
    mocker.patch("exemplo_01.random.randint", new=mock_randint)
    # 3. Execução e Verificação
    assert gerar_id_composto() == expected_id
    # Garante que a função interna foi chamada 4 vezes (uma para cada dígito)
    assert mock_randint.call_count == 4


def test_resultado_absurdo(mocker):
    resultado = 10
    mocker.patch(
        "test_exemplo_01.jogar_dado_seis_lados",
        return_value=resultado,
    )
    assert jogar_dado_seis_lados() == 10


def test_numero_secreto_ok(mocker):
    resultado = 6
    mocker.patch(
        "exemplo_01.jogar_dado_seis_lados",
        return_value=resultado,
    )
    assert verificar_numero_secreto(6)


def test_numero_secreto_erro_num_10(mocker):
    resultado = 10
    mocker.patch(
        "exemplo_01.jogar_dado_seis_lados",
        return_value=resultado,
    )
    assert not verificar_numero_secreto(6)


def test_func_erro_com_bool():
    assert func(True) == "Valor inválido"
    assert func(None) == "Valor inválido"
