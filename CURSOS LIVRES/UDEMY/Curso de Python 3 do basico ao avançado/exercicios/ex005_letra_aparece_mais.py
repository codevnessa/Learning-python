# Frase inicial que vamos analisar
frase = "Python é uma linguagem de programação multi paradigma."

# Converte a frase para letras minúsculas (para não diferenciar maiúsculas de minúsculas)
# e remove todos os espaços em branco (para contar apenas letras)
frase = frase.lower().replace(' ', '')

# Cria um dicionário vazio para armazenar a contagem de cada letra
contagem = {}

# Percorre cada letra da frase
for letra in frase:
    # Se a letra já estiver no dicionário, aumenta sua contagem em 1
    if letra in contagem:
        contagem[letra] += 1
    # Se a letra não estiver no dicionário, adiciona ela com a contagem 1
    else:
        contagem[letra] = 1

# Inicializa variáveis para guardar a letra mais frequente e quantas vezes ela apareceu
letra_mais_frequente = ''
quantidade_mais_frequente = 0

# Percorre o dicionário de contagem para encontrar a letra mais frequente
for letra, quantidade in contagem.items():
    # Se a quantidade da letra atual for maior que a quantidade mais frequente registrada até agora,
    # atualiza a letra mais frequente e a quantidade mais frequente
    if quantidade > quantidade_mais_frequente:
        letra_mais_frequente = letra
        quantidade_mais_frequente = quantidade

# Mostra o resultado: a letra que mais apareceu e quantas vezes ela apareceu
print(f"A letra que mais apareceu foi '{letra_mais_frequente}', {quantidade_mais_frequente} vezes.") 