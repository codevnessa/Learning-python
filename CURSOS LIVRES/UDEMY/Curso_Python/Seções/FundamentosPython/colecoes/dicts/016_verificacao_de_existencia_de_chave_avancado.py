
# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Exemplo 1: Usando `get()` com valor padrão
profissao = dicionario.get("profissao", "Desconhecida")
print("Profissão:", profissao)

# Exemplo 2: Verificando múltiplas chaves
chaves_verificar = ["nome", "profissao", "cidade"]
for chave in chaves_verificar:
    if chave in dicionario:
        print(f"A chave '{chave}' existe com valor: {dicionario[chave]}")
    else:
        print(f"A chave '{chave}' não existe.")

"""
Explicação:
- No Exemplo 1, usamos `get()` com um valor padrão para evitar erros ao acessar chaves que podem não existir.
- No Exemplo 2, verificamos a existência de múltiplas chaves em um loop, o que é útil para verificar várias chaves de uma vez.

Essas técnicas são úteis para garantir que o código não quebre ao acessar chaves que podem não estar presentes no dicionário.
"""