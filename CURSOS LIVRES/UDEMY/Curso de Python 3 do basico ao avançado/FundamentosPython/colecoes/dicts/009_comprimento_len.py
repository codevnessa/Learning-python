"""
O comprimento de um dicionário é o número de pares chave-valor que ele contém.
"""

# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Obtendo o comprimento do dicionário
comprimento = len(dicionario)

print("Comprimento do dicionário:", comprimento)

"""
Explicação:
- A função `len()` retorna o número de pares chave-valor no dicionário.
- No exemplo acima, o dicionário tem 3 pares chave-valor, então `len(dicionario)` retorna 3.
"""