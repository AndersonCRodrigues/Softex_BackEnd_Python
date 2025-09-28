from .Model import Model


class Usuario(Model):
    """
    Modelo de Usuario.
    Demonstra herança e encapsulamento.
    """

    def __init__(self, id: int, nome: str, email: str):
        super().__init__(id)  # Herança: chama o construtor da superclass
        self.nome: str = nome
        self.__email: str = email  # Atributo privado

    @property
    def email(self) -> str:
        """Getter para o atributo privado __email usando @property."""
        return self.__email

    @email.setter
    def email(self, novo_email: str) -> None:
        """
        Setter para o atributo privado __email.
        Versão simplificada sem 'raise'.
        """
        if "@" not in novo_email:
            print("AVISO: Email inválido. O valor não foi alterado.")
            return
        self.__email = novo_email

    def __str__(self) -> str:
        return f"Usuário(id={self.id}, nome='{self.nome}', email='{self.email}')"
