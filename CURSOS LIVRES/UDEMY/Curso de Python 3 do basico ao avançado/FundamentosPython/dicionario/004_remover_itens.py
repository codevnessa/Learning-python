"""
Existem várias maneiras de remover itens de um dicionário:
1. Usando a palavra-chave `del`.
2. Usando o método `pop()`.
3. Usando o método `popitem()`.
"""

# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

print("Dicionário antes da remoção:\n", dicionario)
print()

# Método 1: Usando `del`
del dicionario["idade"]
print("Dicionário após remoção com `del`:\n", dicionario)
print()

# Método 2: Usando `pop()`
cidade = dicionario.pop("cidade")
print("Dicionário após remoção com `pop()`:\n", dicionario)
print("Valor removido com `pop()`:\n", cidade)
print()


# Método 3: Usando `popitem()`
item_removido = dicionario.popitem()
print("Dicionário após remoção com `popitem()`:\n", dicionario)
print("Item removido com `popitem()`:\n", item_removido)

"""
Explicação:
- `del dicionario[chave]`: Remove o item com a chave especificada. Se a chave não existir, um erro KeyError será levantado.
- `dicionario.pop(chave)`: Remove o item com a chave especificada e retorna o valor. Se a chave não existir, um erro KeyError será levantado.
- `dicionario.popitem()`: Remove e retorna o último item inserido no dicionário. Se o dicionário estiver vazio, um erro KeyError será levantado.
"""