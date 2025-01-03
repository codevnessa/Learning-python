"""
Para atualizar um valor, basta atribuir um novo valor a uma chave existente.
"""

# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

print("Dicionário antes da atualização:", dicionario)

# Atualizando o valor da chave "idade"
dicionario["idade"] = 26

print("Dicionário após atualização:", dicionario)

"""
Explicação:
- Para atualizar um valor em um dicionário, basta atribuir um novo valor a uma chave existente, como em dicionario["idade"] = 26.
- Se a chave não existir, ela será criada, mas isso é mais relacionado à adição de pares chave-valor.
"""