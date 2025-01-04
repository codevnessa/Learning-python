"""
Para acessar um valor em um dicionário, basta usar a chave correspondente.
Se a chave não existir, um erro KeyError será levantado.
"""

# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando valores por chave
nome = dicionario["nome"]
idade = dicionario["idade"]
cidade = dicionario["cidade"]

print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)

# Tentando acessar uma chave que não existe 
# profissao = dicionario["profissao"]  
# Isso levantaria um KeyError

"""
Explicação:
- Para acessar um valor em um dicionário, usamos a sintaxe dicionario[chave].
- Se a chave não existir, um erro KeyError será levantado. Para evitar isso, podemos usar o método get()
"""