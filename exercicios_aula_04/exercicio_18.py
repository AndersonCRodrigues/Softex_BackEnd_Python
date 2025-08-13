email = input("Digite seu e-mail: ")

if "@" in email and "." in email:
    if (
        not email.startswith("@")
        and not email.startswith(".")
        and not email.endswith("@")
        and not email.endswith(".")
        and " " not in email
    ):
        print("E-mail válido!")
    else:
        print("E-mail inválido!")
else:
    print("E-mail inválido!")
