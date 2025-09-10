def exibir_pedido(item: str, *extras: str, **observacoes: str) -> None:
    print(f"Item Principal: {item}")
    print(f"Extras: {extras}")
    print(f"Observações: {observacoes}")


exibir_pedido( "Queijo extra","Bacon","Pizza", borda="recheada", ingrediente="tomate")
