# Explicação do conteúdo: Uma matriz nula é uma matriz preenchida com zeros.
# Podemos criar uma matriz nula usando list comprehension.

# Exemplo de criação de uma matriz nula:
linhas = 3
colunas = 3
nula = [[0 for _ in range(colunas)] for _ in range(linhas)]
print("Matriz nula:", nula)

# Explicação do código:
# 1. A list comprehension cria uma matriz preenchida com zeros.
# OBS: A matriz nula é útil como ponto de partida para operações matemáticas.