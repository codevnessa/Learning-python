# Explicação do conteúdo: Podemos adicionar uma nova linha à matriz usando o método append() ou remover uma linha usando o método pop().

# Exemplo de adição e remoção de linhas:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz.append([10, 11, 12])  # Adiciona uma nova linha
print("Matriz após adicionar linha:", matriz)

matriz.pop(1)  # Remove a segunda linha
print("Matriz após remover linha:", matriz)

# Explicação do código:
# 1. append([10, 11, 12]) adiciona uma nova linha ao final da matriz.
# 2. pop(1) remove a segunda linha (índice 1) da matriz.
# OBS: pop() também pode ser usado sem argumentos para remover a última linha.