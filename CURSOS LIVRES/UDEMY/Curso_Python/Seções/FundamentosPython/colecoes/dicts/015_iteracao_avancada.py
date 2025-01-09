
# Criando um dicionário de exemplo
dicionario = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

# Exemplo 1: Iterar sobre chaves e valores ao mesmo tempo
print("Iterando sobre chaves e valores:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# Exemplo 2: Iterar sobre chaves e aplicar uma função aos valores
print("\nIterando sobre chaves e aplicando uma função aos valores:")
for chave in dicionario:
    print(f"{chave}: {dicionario[chave] * 2}")

# Exemplo 3: Iterar sobre dicionários aninhados
dicionario_aninhado = {
    "pessoa1": {"nome": "Alice", "idade": 25},
    "pessoa2": {"nome": "Bob", "idade": 30}
}

print("\nIterando sobre dicionários aninhados:")
for pessoa, dados in dicionario_aninhado.items():
    print(f"{pessoa}:")
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

"""
Explicação:
- No Exemplo 1, iteramos sobre os pares chave-valor usando `items()`.
- No Exemplo 2, iteramos sobre as chaves e aplicamos uma função (multiplicação por 2) aos valores.
- No Exemplo 3, iteramos sobre um dicionário aninhado, acessando os dados internos de cada pessoa.

Iteração avançada é útil para manipular e acessar dados complexos em dicionários.
"""