# Criando uma lista de listas
lista_aninhada = [[x for x in range(3)] for _ in range(2)]

# Exibindo a lista
print(lista_aninhada)  # Resultado: [[0, 1, 2], [0, 1, 2]]

# 1. `[[x for x in range(3)] for _ in range(2)]` cria duas sublistas.
# 2. Cada sublista contém números de 0 a 2.
# 3. `print(lista_aninhada)` exibe a lista.