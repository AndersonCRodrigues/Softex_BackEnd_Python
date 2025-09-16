from combate import batalha
from personagem import Personagem


heroi = Personagem("Aragorn", 100, 15, pocoes=1)
monstro = Personagem("Dragão", 150, 20)

batalha(heroi, monstro)
