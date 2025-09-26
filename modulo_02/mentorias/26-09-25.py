"""
    Nível Médio/Avançado: Hierarquia de Formas Geométricas

Crie uma classe base FormaGeometrica com um construtor para cor e um método
calcular_area() que não faz nada.
Crie uma classe Retangulo que herda de FormaGeometrica e tem atributos para largura e
altura. A classe deve sobrescrever o método calcular_area().
Crie uma classe Quadrado que herda de Retangulo. O construtor deve receber apenas o lado
e passar esse mesmo valor para largura e altura da classe pai. O encapsulamento deve ser
aplicado aos atributos de dimensão.
No script principal, crie uma tupla com um objeto de Retangulo e um objeto de Quadrado.
Crie uma função chamada calcular_soma_areas() que recebe essa tupla, itera sobre ela e
soma a área de todas as formas. A função deve chamar o método calcular_area() de forma
polimórfica para cada objeto, exibindo a soma total no final.
"""
