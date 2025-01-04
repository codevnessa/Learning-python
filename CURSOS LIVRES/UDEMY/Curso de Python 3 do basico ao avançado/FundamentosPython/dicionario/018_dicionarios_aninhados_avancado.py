
# Criando um dicionário aninhado de exemplo
dicionario = {
    "pessoa1": {
        "nome": "Alice",
        "idade": 25,
        "endereco": {
            "rua": "Rua A",
            "cidade": "São Paulo"
        }
    },
    "pessoa2": {
        "nome": "Bob",
        "idade": 30,
        "endereco": {
            "rua": "Rua B",
            "cidade": "Rio de Janeiro"
        }
    }
}

# Acessando valores profundamente aninhados
print("Cidade da pessoa1:", dicionario["pessoa1"]["endereco"]["cidade"])

# Modificando valores profundamente aninhados
dicionario["pessoa2"]["endereco"]["cidade"] = "Belo Horizonte"
print("Dicionário após modificação:", dicionario)

# Iterando sobre dicionários profundamente aninhados
print("\nIterando sobre dicionários aninhados:")
for pessoa, dados in dicionario.items():
    print(f"{pessoa}:")
    for chave, valor in dados.items():
        if isinstance(valor, dict):
            print(f"  {chave}:")
            for subchave, subvalor in valor.items():
                print(f"    {subchave}: {subvalor}")
        else:
            print(f"  {chave}: {valor}")

"""
Explicação:
- No exemplo acima, acessamos e modificamos valores profundamente aninhados no dicionário.
- Também iteramos sobre dicionários aninhados, verificando se um valor é outro dicionário usando `isinstance(valor, dict)`.

Essas técnicas são úteis para trabalhar com estruturas de dados complexas e profundamente aninhadas.
"""