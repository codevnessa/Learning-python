# Lista contendo elementos de vários tipos
lista = [
    'a',  # String
    1,    # Inteiro
    1.1,  # Float
    True, # Booleano
    [0, 1, 2],  # Lista
    (1, 2),     # Tupla
    {0, 1},     # Conjunto (set)
    {'nome': 'Luiz'},  # Dicionário
]

# Itera sobre cada item da lista
for item in lista:
    # Verifica se o item é um conjunto (set)
    if isinstance(item, set):
        print('SET')  # Indica que o item é um conjunto
        item.add(5)   # Adiciona o número 5 ao conjunto
        print(item, isinstance(item, set))  # Imprime o conjunto atualizado e confirma que ainda é um set

    # Verifica se o item é uma string (str)
    elif isinstance(item, str):
        print('STR')  # Indica que o item é uma string
        print(item.upper())  # Converte a string para maiúsculas e imprime

    # Verifica se o item é um número (int ou float)
    elif isinstance(item, (int, float)):
        print('NUM')  # Indica que o item é um número
        print(item, item * 2)  # Imprime o número e seu dobro
 
    # Caso o item não seja nenhum dos tipos anteriores
    else:
        print('OUTRO')  # Indica que o item é de outro tipo
        print(item)  # Imprime o item sem modificações