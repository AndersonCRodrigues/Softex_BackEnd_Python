class Model:
    """Classe base que define o comportamento padrão para todos os modelos."""

    def __init__(self, id: int):
        self._id: int = id

    @property
    def id(self) -> int:
        """Getter para o atributo protegido _id."""
        return self._id
