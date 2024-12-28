# Explicação do conteúdo: Tuplas são frequentemente usadas em funções built-in do Python, como zip(), enumerate() e map().
# Essas funções retornam ou manipulam tuplas, tornando-as úteis em várias situações.

# Exemplo de uso de tuplas com zip() e enumerate():
nomes = ["Maria", "João", "Pedro"]
idades = [30, 25, 35]

# zip() combina duas listas em uma lista de tuplas
combinados = list(zip(nomes, idades))
print("Combinação de nomes e idades:", combinados)

# enumerate() retorna pares de índice e valor como tuplas
for indice, nome in enumerate(nomes):
    print(f"Índice: {indice}, Nome: {nome}")

# Explicação do código:
# 1. zip() combina as listas `nomes` e `idades` em uma lista de tuplas.
# 2. enumerate() retorna tuplas contendo o índice e o valor de cada elemento da lista.
# OBS: Tuplas são úteis em funções built-in por serem imutáveis e eficientes.