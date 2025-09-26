def calc(num_1: float, num_2: float) -> tuple[float, float]:
    div = num_1 / num_2
    mult = num_1 * num_2
    return div, mult


resposta1, resposta2 = calc(2.5, 5.2)
print(f"{resposta1:.3f}")
print(resposta2)
