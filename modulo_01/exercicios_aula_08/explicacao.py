num = "2197066124"
valido =True
for c in num:
    contador_repetidos = 0
    for d in num:
        print(f"num C {c} num D {d} são inguais? {c==d}")
        if c==d:
            contador_repetidos+=1
        if contador_repetidos >= 3:
            print("Numero não é valido")
            valido = False
            break