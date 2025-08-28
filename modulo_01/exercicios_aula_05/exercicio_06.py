senha = ""
for i in range(3):
    palavra = input(f"Digite a {i+1}ª palavra: ")
    senha += palavra
senha_final = senha + str(len(senha))
print(f"Sua senha gerada é: {senha_final}")
