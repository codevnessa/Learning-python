"""
Podemos usar o operador `in` para verificar a existência de uma chave.
"""

# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Verificando a existência de chaves
print("A chave 'nome' existe?", "nome" in dicionario)
print("A chave 'profissao' existe?", "profissao" in dicionario)

"""
Explicação:
- O operador `in` retorna `True` se a chave existir no dicionário e `False` caso contrário.
- Essa verificação é útil para evitar erros ao acessar chaves que podem não existir.
"""