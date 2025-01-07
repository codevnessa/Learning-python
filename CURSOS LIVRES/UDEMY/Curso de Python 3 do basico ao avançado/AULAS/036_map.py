# Importações necessárias
from functools import partial  # Para criar funções parcialmente aplicadas


# Função para imprimir um iterador de forma organizada
def print_iter(iterator):
    print(*list(iterator), sep='\n')  # Converte o iterador em lista e imprime cada item em uma nova linha
    print() 

# Função para calcular um aumento percentual em um valor
def aumento(valor, porcentagem):
    return round(valor * porcentagem, 2) 

# Cria uma função parcial "aumentar" que aplica um aumento de 10% (1.1) ao valor
aumentar = partial(
    aumento, porcentagem=1.1  # Fixa o argumento "porcentagem" como 1.1
)

# Lista de produtos com seus nomes e preços
produtos = [
    {'nome': 'Café', 'preco': 10.00},
    {'nome': 'Arroz', 'preco': 22.32},
    {'nome': 'Açucar', 'preco': 10.11},
    {'nome': 'Azeite', 'preco': 105.87},
    {'nome': 'Car', 'preco': 69.90},
]

# Função para atualizar o preço de um produto usando a função "aumentar"
def atualiza(produto):
    return {
        **produto,  # Mantém todos os dados originais do produto
        'preco': aumentar(produto['preco'])  # Aplica o aumento de 10% ao preço
    }

# Usa a função map para aplicar a função "atualiza" a cada produto na lista
novos_produtos = list(map(
    atualiza,  # Função a ser aplicada
    produtos  # Iterável (lista de produtos)
))

# Exibe a lista original de produtos
print("Produtos originais:")
print_iter(produtos)

# Exibe a lista de produtos com os preços atualizados
print("Produtos com aumento de 10%:")
print_iter(novos_produtos)

print("Exemplo de map com lambda:")
print(
    list(
        map(
            lambda x: x * 3,  # Função lambda que multiplica por 3
            [1, 2, 3, 4]  # Lista de números
        )
    )
)

"""
- map é útil para transformar dados em um iterável.
- partial simplifica a criação de funções com argumentos fixos.
- lambda é ideal para operações rápidas e simples.
- Iteradores são eficientes, mas devem ser usados com cuidado devido ao esgotamento.
"""