"""
Crie duas classes: Livro e Biblioteca. 
1.  A classe Livro terá atributos título e autor. 
2.  A classe Biblioteca terá um atributo acervo, que começa como uma lista vazia []. 
3.  A Biblioteca deve ter dois métodos: 
○  adicionar_livro(livro): recebe um objeto Livro e o adiciona à lista acervo. 
○  listar_livros(): percorre a lista acervo e imprime o título e o autor de cada livro. 
Crie uma biblioteca, crie alguns objetos Livro e adicione-os à biblioteca. Depois, liste os livros. 
 
"""
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"O livro {self.titulo} é do autor {self.autor}"

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livros(self, livro:Livro):
        self.acervo.append(livro)

    def listar_livro(self):
        for livro in self.acervo:
            print(livro)

livro1 = Livro("titulo1", "autor1")
livro2 = Livro("titulo2", "autor2")
biblioteca = Biblioteca()
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)
biblioteca.listar_livro()