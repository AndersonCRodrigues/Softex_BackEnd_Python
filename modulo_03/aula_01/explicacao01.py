materias:dict[str, list[float]] = {}

def add_nota_materia(materia: str, nota:float):
    aula = materias.get(materia)
    print(f"aula atual: {aula}")
    if aula:
        aula.append(nota)
    else:
        materias[materia] = [nota]
    
    print(f"dicionario de materias: {materias}")

add_nota_materia("matematica", 10.0)
add_nota_materia("matematica", 9.0)


