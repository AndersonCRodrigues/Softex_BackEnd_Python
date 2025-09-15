def autenticar_usuario(
        dados_banco:dict, 
        conta:str,
        senha:str,
        ) -> tuple[bool, dict | None]:
    """Autentica o usuario com base na conta e senha. Retorna o status e o usuario"""
    usuario_encontrado = dados_banco["usuarios"].get(conta, None) # None == nada

    if usuario_encontrado and usuario_encontrado["senha"] == senha:
        return True, usuario_encontrado
    
    return False, None