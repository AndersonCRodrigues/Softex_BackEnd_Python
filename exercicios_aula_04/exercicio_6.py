texto = input("Digite um texto: ")
letra = input("Digite a letra que deseja contar: ")

quantidade = texto.lower().count(letra.lower())
print(f"A letra '{letra}' aparece {quantidade} vezes.")
