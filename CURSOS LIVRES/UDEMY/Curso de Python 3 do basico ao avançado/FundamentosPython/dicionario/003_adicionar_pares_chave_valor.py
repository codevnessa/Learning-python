"""
Para adicionar um novo par chave-valor, basta atribuir um valor a uma nova chave.
Se a chave já existir, o valor será atualizado.
"""

# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25
}

print("Dicionário antes da adição:\n", dicionario)
print()

# Adicionando um novo par chave-valor
dicionario["cidade"] = "São Paulo"

print("Dicionário após adição:\n", dicionario)
print()

# Atualizando um valor existente
dicionario["idade"] = 26

print("Dicionário após atualização:\n", dicionario)
print()


"""
Explicação:
- Para adicionar um novo par chave-valor, basta atribuir um valor a uma nova chave, como em dicionario["cidade"] = "São Paulo".
- Se a chave já existir, o valor será atualizado, como em dicionario["idade"] = 26.
"""