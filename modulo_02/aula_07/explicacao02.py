class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self.set_preco(preco)

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, valor):
        if self._verifica_valor(valor):
            self.__preco = valor
        else:
            print("Valor incorreto!")

    def _verifica_valor(self, valor):
        return valor >= 0
    
caneta = Produto("Caneta Azul", 0)
print("primeiro get")
print(caneta.get_preco())
caneta.set_preco(10)
print("segundo get")
print(caneta.get_preco())
print("terceiro get")
caneta.set_preco(-10)
print(caneta.get_preco())
