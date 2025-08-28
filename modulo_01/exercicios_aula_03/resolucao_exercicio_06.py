"""
6. Peça ao usuario para entrar com uma palavra
- Ela tem que começar com "P".
- Ela tem que terminar com "S".
- A palavra deve conter a letra "I" em qualquer posição.
- A palavra NÃO deve conter "M" nem "N".
- Ela deve ter no mínimo 3 caracteres.
- A palavra deve ser toda em minusculo.
- O programa deve executar até que as condições sejam atendidas.
"""

while True:
    palavra = input("Digite uma palavra: ").lower()
    if len(palavra) < 3:
        print("A palavra deve ter no mínimo 3 caracteres.")
    elif palavra[0] != 'p':
        print("A palavra deve começar com 'P'.")
    elif palavra[len(palavra) - 1] != "s":
        print("A palavra deve terminar com 'S'.")
    elif "i" not in palavra:
        print("A palavra deve conter a letra 'I'.")
    elif "m" in palavra or "n" in palavra:
        print("A palavra não deve conter 'M' nem 'N'.")
    else:
        print(f"A palavra '{palavra}' atende a todas as condições!")
        break
