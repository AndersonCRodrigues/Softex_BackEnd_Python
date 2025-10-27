def somar(a, b): 
    return a + b 

def subtrair(a, b): 
    return a - b 

def processar_lista(lista): 
    """Ordena uma lista, levantando erro se vazia.""" 
    if not lista: 
        raise ValueError("Lista não pode ser vazia.") 
    return sorted(lista)  