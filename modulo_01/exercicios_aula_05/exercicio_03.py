maior = float(-100000000)
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    if num > maior:
        maior = num
print(f"O maior número é: {maior}")
