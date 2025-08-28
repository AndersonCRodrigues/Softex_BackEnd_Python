palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
palavra_invertida = ""
for i in range(len(palavra) - 1, -1, -1):
    palavra_invertida += palavra[i]
if palavra.lower() == palavra_invertida.lower():
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
