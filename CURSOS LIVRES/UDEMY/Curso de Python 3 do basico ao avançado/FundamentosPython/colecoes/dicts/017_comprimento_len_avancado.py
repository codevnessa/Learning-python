# Criando um dicionário de exemplo
dicionario = {
    "pessoa1": {"nome": "Alice", "idade": 25},
    "pessoa2": {"nome": "Bob", "idade": 30},
    "pessoa3": {"nome": "Charlie", "idade": 35}
}

# Obtendo o comprimento do dicionário principal
comprimento_principal = len(dicionario)
print("Comprimento do dicionário principal:", comprimento_principal)

# Obtendo o comprimento de um dicionário aninhado
comprimento_aninhado = len(dicionario["pessoa1"])
print("Comprimento do dicionário aninhado (pessoa1):", comprimento_aninhado)

# Combinando dicionários e obtendo o comprimento
dicionario2 = {"pessoa4": {"nome": "David", "idade": 40}}
dicionario_combinado = {**dicionario, **dicionario2}
comprimento_combinado = len(dicionario_combinado)
print("Comprimento do dicionário combinado:", comprimento_combinado)

"""
Explicação:
- `len()` pode ser usado para obter o número de pares chave-valor em um dicionário, seja ele principal ou aninhado.
- No exemplo acima, combinamos dois dicionários usando `{**dicionario, **dicionario2}` e obtemos o comprimento do dicionário resultante.

Essa técnica é útil para verificar o tamanho de estruturas de dados complexas.
"""