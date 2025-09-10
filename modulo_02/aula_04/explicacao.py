def exibir_pedido(item: str, *extras: str, **observacoes: str) -> None:
    print(f"Item Principal: {item}")
    print(f"Extras: {extras}")
    print(f"Observações: {observacoes}")


exibir_pedido( "Pizza", "Queijo extra","Bacon", borda="recheada", ingrediente="tomate")
