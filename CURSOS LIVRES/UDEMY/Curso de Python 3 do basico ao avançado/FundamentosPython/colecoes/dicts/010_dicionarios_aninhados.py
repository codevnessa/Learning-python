"""
Dicionários aninhados são dicionários que contêm outros dicionários como valores.
"""

# Criando um dicionário aninhado
dicionario = {
    "pessoa1": {
        "nome": "Alice",
        "idade": 25,
        "cidade": "São Paulo"
    },
    "pessoa2": {
        "nome": "Bob",
        "idade": 30,
        "cidade": "Rio de Janeiro"
    }
}

# Acessando valores em dicionários aninhados
print("Nome da pessoa1:", dicionario["pessoa1"]["nome"])
print("Idade da pessoa2:", dicionario["pessoa2"]["idade"])

# Adicionando um novo dicionário aninhado
dicionario["pessoa3"] = {"nome": "Charlie", "idade": 35, "cidade": "Belo Horizonte"}

print("Dicionário após adição:", dicionario)

"""
Explicação:
- Dicionários aninhados são úteis para representar estruturas de dados mais complexas.
- Para acessar valores em dicionários aninhados, usamos múltiplos colchetes, como em dicionario["pessoa1"]["nome"].
- Podemos adicionar novos dicionários aninhados da mesma forma que adicionamos pares chave-valor em um dicionário simples.
"""