def calc(num_1: float, num_2: float) -> tuple[float, float]:
    div = num_1 / num_2
    mult = num_1 * num_2
    print(div, mult)
    return div, mult


variavel = calc(2.5, 5.2)


def calc2(a, b):
    div = a / b
    mult = a * b
    print(div, mult)
    return div, mult


calc2(4, 5)
c, d = calc2()
e = c**d
print(e)
