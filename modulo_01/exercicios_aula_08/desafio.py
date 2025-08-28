lA = input("Entrada do lado A: ")
lB = input("Entrada do lado B: ")
lC = input("Entrada do lado C: ")

if lA.isdigit() and lB.isdigit() and lC.isdigit():
    lA = int(lA)
    lB = int(lB)
    lC = int(lC)

    if lA <= 0 or lB <= 0 or lC <= 0:
        print("Entradas inválidas. Os lados devem ser números positivos.")
        exit()
else:
    print("Entradas inválidas. Por favor, insira números inteiros positivos.")
    exit()

soma_ok = True
if lA > lB + lC:
    soma_ok = False
if lB > lA + lC:
    soma_ok = False
if lC > lA + lB:
    soma_ok = False

dif_ok = True
if lA < abs(lB - lC):
    dif_ok = False
if lB < abs(lA - lC):
    dif_ok = False
if lC < abs(lA - lB):
    dif_ok = False

if soma_ok and dif_ok:
    print(f"Os lados {lA}, {lB} e {lC} podem formar um triângulo.")
else:
    print(f"Os lados {lA}, {lB} e {lC} não podem formar um triângulo.")
