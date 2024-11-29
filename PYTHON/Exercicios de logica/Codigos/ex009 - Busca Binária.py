# Define a função busca_binaria que realiza uma busca binária em uma lista ordenada
def busca_binaria(lista, alvo):
    # Inicializa os índices esquerda e direita
    esquerda, direita = 0, len(lista) - 1
    
    # Loop enquanto o índice esquerda for menor ou igual ao índice direita
    while esquerda <= direita:
        # Calcula o índice do meio
        meio = (esquerda + direita) // 2
        
        # Se o elemento do meio for igual ao alvo, retorna o índice do meio
        if lista[meio] == alvo:
            return meio
        # Se o elemento do meio for menor que o alvo, ajusta o índice esquerda
        elif lista[meio] < alvo:
            esquerda = meio + 1
        # Se o elemento do meio for maior que o alvo, ajusta o índice direita
        else:
            direita = meio - 1
    
    # Se o alvo não for encontrado, retorna -1
    return -1

# Define uma lista ordenada de números
lista = [1, 3, 5, 7, 9, 11, 13]

# Define o número que deseja buscar na lista
alvo = 7

# Realiza a busca binária na lista para encontrar o alvo
indice = busca_binaria(lista, alvo)

# Verifica se o alvo foi encontrado e exibe a mensagem correspondente
if indice != -1:
    print(f"O número {alvo} foi encontrado no índice {indice}.")
else:
    print(f"O número {alvo} não foi encontrado na lista.")