"""
Objetivo: Usar um setter para validar dados numéricos e ter métodos que usam 
a property. 

●  Requisitos: 
1.  Crie uma classe Circulo com um atributo protegido _raio. 
2.  Crie uma @property para raio. 
3.  Crie um @raio.setter que valide se o valor do raio é um número positivo. 
4.  Crie um método calcular_area() que use a propriedade self.raio para retornar 
a área do círculo (A=π⋅r2).
"""
from math import pi
# forma alternativa = import math -> use math.py

class Circulo:
    def __init__(self, raio:int):
        if raio < 0:
            print("O Raio não pode ser negativo")
            self._raio = 0
        else:
            self._raio = raio
    
    @property
    def raio(self) -> int:
        return self._raio
    
    @raio.setter
    def raio(self, novo_raio:int) -> None:
        if novo_raio > 0 and isinstance(novo_raio, int):
            self._raio = novo_raio
        else:
            print("Erro! O novo raio deve ser positivo e inteiro.")

    def calcular_area(self) -> None:
        area = pi * self.raio ** 2
        print(area)
    
roda = Circulo(2)
print(roda.raio)
roda.raio = 3
roda.calcular_area()