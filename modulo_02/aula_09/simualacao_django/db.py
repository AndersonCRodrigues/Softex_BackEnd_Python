import random
from typing import Dict
from Usuarios import Usuario
from Postagem import Postagem




# Dicionários que funcionam como um banco de dados
# As anotações de tipo indicam que as chaves são 'int' e os valores são 'Usuario' ou 'Postagem'
db_usuarios: Dict[int, Usuario] = {}
db_postagens: Dict[int, Postagem] = {}


def gerar_id_aleatorio(db: Dict) -> int:
    """Função auxiliar para gerar um ID numérico único de 6 dígitos."""
    id_gerado: int = 0
    # Garante que o ID não é zero e não está em uso no 'banco de dados'
    while id_gerado == 0 or id_gerado in db:
        id_gerado = random.randint(100000, 999999)
    return id_gerado
