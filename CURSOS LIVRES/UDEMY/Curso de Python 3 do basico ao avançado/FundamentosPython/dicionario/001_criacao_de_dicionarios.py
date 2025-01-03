"""
Um dicionário é uma coleção de pares chave-valor, onde cada chave é única.
Os dicionários são mutáveis, ou seja, podem ser alterados após a criação.

Existem várias maneiras de criar dicionários em Python:
1. Usando chaves {} e pares chave-valor.
2. Usando a função dict().
3. Usando compreensão de dicionários (será abordado em outro arquivo).
"""

# Método 1: Usando chaves {} e pares chave-valor
dicionario1 = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

print("Dicionário 1:\n", dicionario1)
print()
# Método 2: Usando a função dict()
dicionario2 = dict(nome="Bob", idade=30, cidade="Rio de Janeiro")

print("Dicionário 2:\n", dicionario2)
print()
# Método 3: Criando um dicionário vazio e adicionando pares chave-valor
dicionario3 = {}
dicionario3["nome"] = "Charlie"
dicionario3["idade"] = 35
dicionario3["cidade"] = "Belo Horizonte"

print("Dicionário 3:", dicionario3)

"""
Explicação:
- No Método 1, criamos um dicionário diretamente usando chaves {} e especificando os pares chave-valor.
- No Método 2, usamos a função dict() para criar um dicionário. Note que as chaves são passadas como argumentos nomeados.
- No Método 3, criamos um dicionário vazio e depois adicionamos os pares chave-valor.

Todos os métodos são válidos e a escolha depende do contexto e da preferência do programador.
"""