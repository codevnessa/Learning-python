from palavras import palavras  # Certifique-se de que o arquivo "palavras.py" existe e contém uma lista chamada "palavras"

# Calcula a quantidade de palavras
qtd_palavras = len(palavras)

# Calcula a quantidade total de letras usando list comprehension
qtd_letras = sum(len(palavra) for palavra in palavras)

# Encontra a maior e a menor palavra usando funções embutidas
maior = max(palavras, key=len).upper()
menor = min(palavras, key=len).upper()

# Exibe os resultados
print("Quantidade de palavras:", qtd_palavras)
print("Quantidade total de letras nas palavras:", qtd_letras)
print("Maior palavra:", maior)
print("Menor palavra:", menor)