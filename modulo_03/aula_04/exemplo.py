updates = ["email = ?", "senha = ?", "data_atualizacao = ?"]
query = f"UPDATE usuarios SET {', '.join(updates)} WHERE id = ?;"

print(query)


f"""
litsa de strings:
{updates}
final da minha string!
"""