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


"""
tenho uma pastaprincial chamada deliveryaapp
deliveryaapp > components > css >  dois arquivos um footer.css e outro menu.css
deliveryaapp > components > html > dois arquvios footer.html e menu.html
deliveryaapp > components > js > dois arquivos um footer.js e menu.js
deliveryaapp > css > com seis arquivos com os sequintes nomes = cart, checkout, confirmation, global, homepage, products
deliveryaapp > html > com cinco arquivos com o seguinte nome = cart, checkout, confirmation, homepage, products
deliveryaapp > js > com cinco arquivos js com o seguinte nome = cart, checkout, confirmation, homepage, products
"""