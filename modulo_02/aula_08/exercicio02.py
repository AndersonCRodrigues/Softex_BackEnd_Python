class Midia:
    def __init__(self, titulo:str, duracao_seg:int):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"Titulo: {self.titulo}, duração: {self.duracao_seg}.")

    def __str__(self):
        return f"{self.titulo}"

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista: str):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"Titulo: {self.titulo}, duração: {self.duracao_seg}, Artista {self.artista}.")

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao:str):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"Titulo: {self.titulo}, duração: {self.duracao_seg}, Resoluçao {self.resolucao}.")


m1 = Musica("Lalala", 30, "Zé")
v1 = Video("Toc-toc", 60, "1600x1200")

dicionarios_midia:dict[str, list[Midia]] = {"musicas":[], "videos":[]}
dicionarios_midia["musicas"].append(m1)
dicionarios_midia["videos"].append(v1)

# print(dicionarios_midia)

for item in dicionarios_midia.values():
    # print(item)
    for midia in item:
        midia.exibir()