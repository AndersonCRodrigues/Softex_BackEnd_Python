produto_info = {"nome": "Smartphone", "cor": "Preto", "estoque": 10}

detalhes_estoque = {"preco": 1500.00, "estoque": 50}

# Usando .update() para adicionar os detalhes de estoque
# produto_info |= detalhes_estoque
# produto_info.update(detalhes_estoque)


# união de dois dicionários fazendo update de chaves e valores
novo_produto = produto_info | detalhes_estoque

print(produto_info)
print(novo_produto)
# Saída: {'nome': 'Smartphone', 'cor': 'Preto', 'preco': 1500.0, 'estoque': 50}
