def banco_dados() -> dict:
    """Carrega os dados inicias do banco dados, que inclui usuario e configurações"""
    return {
        "usuarios": {
            "123456-7": {
                "senha": "9999",
                "nome": "José",
                "saldo": 1500.00,
                "limite_cheque_especial": 500.00,
            },
        },
        "tentavas_login": 3,
        "ultima_conta_base": "123456",
        "digito_verificador": "7",
    }