# Exemplo 1: Criar um dicionário com valores condicionais
numeros = [1, 2, 3, 4, 5]
dicionario1 = {n: "par" if n % 2 == 0 else "ímpar" for n in numeros}

print("Dicionário 1:", dicionario1)

# Exemplo 2: Criar um dicionário a partir de duas listas com condicionais
chaves = ["a", "b", "c", "d"]
valores = [1, 2, 3, 4]
dicionario2 = {k: v for k, v in zip(chaves, valores) if v % 2 == 0}

print("Dicionário 2:", dicionario2)

# Exemplo 3: Criar um dicionário com funções aplicadas aos valores
dicionario3 = {n: n**2 for n in range(5)}

print("Dicionário 3:", dicionario3)

"""
Explicação:
- No Exemplo 1, usamos uma condicional dentro da compreensão de dicionários para atribuir valores diferentes com base na paridade do número.
- No Exemplo 2, usamos uma condicional para filtrar quais pares chave-valor serão incluídos no dicionário.
- No Exemplo 3, aplicamos uma função (n**2) aos valores do dicionário.

Compreensão de dicionários é uma ferramenta poderosa para criar dicionários de forma concisa e legível, especialmente quando combinada com condicionais e funções.
"""