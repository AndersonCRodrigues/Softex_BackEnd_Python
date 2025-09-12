"""
7.  Conversor de Temperatura: Crie uma função que receba uma temperatura em
Celsius e a converta para Fahrenheit. A fórmula é: F = (C * 9/5) + 32
"""


def celsius_fahrenheit(temperatura_c: float) -> float:
    return (temperatura_c * (9 / 5)) + 32


temperatura_celsius = float(input("Entre com a temperatura em Celsius: "))
temperatura_f = celsius_fahrenheit(temperatura_celsius)
print(
    f"A temperatura {temperatura_celsius:.2f}°C "
    f"em Fahrenheit fica em {temperatura_f:.2f}°F"
)
