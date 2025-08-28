idade = int(input("Digite a idade: "))
tem_cnh_input = input("Você tem CNH? (s/n): ")
tem_cnh = tem_cnh_input.lower() == "s"

if idade >= 18 and tem_cnh:
    print("Pode dirigir.")
elif idade >= 18 and not tem_cnh:
    print("Precisa tirar a CNH.")
else:
    print("Não pode dirigir.")
