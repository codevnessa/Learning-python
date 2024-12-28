# Tipos de Exceções
# Em Python, existem muitos tipos de exceções que podem ser geradas. Cada tipo de erro tem um nome específico, como:
# ZeroDivisionError: Ocorre quando há uma divisão por zero.
# TypeError: Ocorre quando uma operação é aplicada a um tipo de dado incompatível.
# ValueError: Ocorre quando um valor inválido é fornecido para uma função ou operação.
# IndexError: Ocorre quando um índice está fora do intervalo de uma lista, tupla ou string.
# KeyError: Ocorre quando uma chave não existe em um dicionário.

# Exemplo:
try:
    lista = [1, 2, 3]
    print(lista[5])  # Isso gera um IndexError
except IndexError:
    print("Erro: índice fora do intervalo!")

# Explicação:
# O código tenta acessar o índice 5 de uma lista que só tem 3 elementos.
# Como o índice 5 não existe, o Python gera um IndexError.
# O bloco except captura o erro e exibe a mensagem "Erro: índice fora do intervalo!".