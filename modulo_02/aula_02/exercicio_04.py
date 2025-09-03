notas = [
    ("Ana", 9.5),
    ("João", 8.0),
    ("Maria", 10.0),
    ("Pedro", 7.5),
    ("Ana", 10.0),
    ("Carlos", 6.5),
]


maior_nota = 0.0
for _, nota in notas:
    if nota > maior_nota:
        maior_nota = nota
print(f"A maior nota alcançada é: {maior_nota}")

alunos_maior_nota = []
for aluno, nota in notas:
    if nota == maior_nota:
        alunos_maior_nota.append(aluno)
alunos_maior_nota = tuple(alunos_maior_nota)
print(f"\nAlunos que tiraram a maior nota: {alunos_maior_nota}")

# alunos_nota_baixa = {aluno for aluno, nota in notas if nota < 7.0}

alunos_nota_baixa = set()
for aluno, nota in notas:
    if nota < 7.0:
        alunos_nota_baixa.add(aluno)

print(f"\nAlunos que tiveram nota menor que 7.0: {alunos_nota_baixa}")
