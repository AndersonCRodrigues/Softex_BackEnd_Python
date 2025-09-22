class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if self._verifica_valor(valor):
            self.__preco = valor
        else:
            print("Valor incorreto!")

    def _verifica_valor(self, valor):
        return valor >= 0
    
caneta = Produto("Caneta Azul", 10)
print(caneta.preco)
caneta.preco = -20
print(caneta.preco)

