# Define a função selection_sort que ordena uma lista de números
def selection_sort(lista):
    # Loop externo para percorrer todos os elementos da lista
    for i in range(len(lista)):
        # Assume que o elemento atual é o menor
        min_idx = i
        # Loop interno para encontrar o menor elemento restante
        for j in range(i+1, len(lista)):
            # Se encontrar um elemento menor, atualiza o índice do menor elemento
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Troca o elemento atual com o menor elemento encontrado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    # Retorna a lista ordenada
    return lista

# Pede ao usuário para digitar os números separados por espaços
entrada = input("Digite os números separados por espaços: ")

# Converte a entrada em uma lista de inteiros
lista = list(map(int, entrada.split()))

# Ordena a lista usando a função selection_sort
lista_ordenada = selection_sort(lista)

# Exibe a lista ordenada
print("Lista ordenada:", lista_ordenada)