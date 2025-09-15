def obter_dados_cliente() -> dict:
    """Solicitar e retornar os dados do cliente"""
    nome = input("Informe seu nome: ")
    return {"nome": nome}