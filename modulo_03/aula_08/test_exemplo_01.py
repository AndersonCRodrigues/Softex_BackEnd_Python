from exemplo_01 import gerar_id_composto, jogar_dado_seis_lados


def test_resultado_dado_seis_lados(mocker):
    resultado = [1, 2, 3]
    resultado_mock = mocker.patch(
        "exemplo_01.random.randint",
        side_effect=resultado,
    )
    assert jogar_dado_seis_lados() == 1
    assert jogar_dado_seis_lados() == 2
    assert jogar_dado_seis_lados() == 3


# def test_gerar_id_composto_sequencial(mocker):

#     sequencia_retornos = [1, 5, 9, 2]

#     mock_randint = mocker.patch(
#         "exemplo_01.random.randint", side_effect=sequencia_retornos
#     )

#     resultado = gerar_id_composto()

#     assert resultado == "1592"

#     assert mock_randint.call_count == 4

#     mock_randint.assert_called_with(1, 9)


# def test_gerar_id_composto_limite_maximo(mocker):

#     sequencia_retornos = [9, 9, 9, 9]

#     mock_randint = mocker.patch(
#         "exemplo_01.random.randint", side_effect=sequencia_retornos
#     )

#     resultado = gerar_id_composto()

#     assert resultado == "9999"
#     assert len(resultado) == 4

#     assert mock_randint.call_count == 4
#     mock_randint.call_args_list[0].assert_called_with(1, 9)

#     mock_randint.assert_called_with(1, 9)
