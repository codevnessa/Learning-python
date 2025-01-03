"""
Podemos iterar sobre as chaves, valores ou pares chave-valor de um dicionário.
"""

# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Iterando sobre as chaves
print("Iterando sobre as chaves:")
for chave in dicionario.keys():
    print(chave)

# Iterando sobre os valores
print("\nIterando sobre os valores:")
for valor in dicionario.values():
    print(valor)

# Iterando sobre os pares chave-valor
print("\nIterando sobre os pares chave-valor:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

"""
Explicação:
- `dicionario.keys()` retorna uma visão das chaves do dicionário.
- `dicionario.values()` retorna uma visão dos valores do dicionário.
- `dicionario.items()` retorna uma visão dos pares chave-valor do dicionário.

Iterar sobre dicionários é uma operação comum e útil para acessar e manipular dados.
"""