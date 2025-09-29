"""
3. Segmento de Reta (Fácil/Médio) 
 
●  Classes: Ponto e SegmentoDeReta. 
●  Classe Ponto: 
○  Atributos: x e y. 
○  Método: __init__(x, y). 
●  Classe SegmentoDeReta: 
○  Atributos (Composição): ponto1 e ponto2, que devem ser instâncias de Ponto. 
○  Método: __init__(ponto1, ponto2). 
○  Método: calcular_comprimento() que retorna a distância entre os dois pontos. 
●  Dica: Use o módulo math e a fórmula da distância euclidiana: 
(x2 −x1 )2+(y2 −y1 )2  
"""
import math

class Ponto:
    def __init__(self, x:int,y:int):
        self.x = x
        self.y = y

class SegmentoDeReta:
    def __init__(self, ponto1: Ponto, ponto2:Ponto):
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def calcular_comprimento(self):
        coord1 = (self.ponto1.x, self.ponto1.y)
        coord2 = (self.ponto2.x, self.ponto2.y)
        resultado = math.dist(coord1, coord2)
        print(resultado)

ponto1 = Ponto(0,2)
ponto2 = Ponto(1,3)
segmento = SegmentoDeReta(ponto1, ponto2)
segmento.calcular_comprimento()