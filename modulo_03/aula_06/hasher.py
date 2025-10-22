# hasher.py
import hashlib


def hash_senha(senha: str) -> str:
    """Gera um hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


def verificar_senha(senha_digitada: str, hash_armazenado: str) -> bool:
    """Verifica se a senha digitada corresponde ao hash no banco."""
    return hash_senha(senha_digitada) == hash_armazenado
