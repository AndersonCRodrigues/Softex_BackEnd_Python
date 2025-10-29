import pytest
from exemplo_02 import gerar_id_composto


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
    Roda o mesmo teste 3 vezes, injetando uma sequência diferente no Mock a cada rodada.
    """
    # 1. Cria o Mock AGORA, usando a sequência fornecida pelo parametrize
    mock_randint = mocker.Mock(side_effect=mock_sequence)
    # 2. Patch: Substitui a função real pelo mock
    mocker.patch("exemplo_02.random.randint", new=mock_randint)
    # 3. Execução e Verificação
    assert gerar_id_composto() == expected_id
    # Garante que a função interna foi chamada 4 vezes (uma para cada dígito)
    assert mock_randint.call_count == 4
