"""
`defaultdict` é uma subclasse de `dict` que fornece um valor padrão para chaves que não existem.
Isso evita erros ao acessar chaves que não foram previamente definidas.
"""

from collections import defaultdict

# Exemplo com dict
dicionario_normal = {}

# Tentando acessar uma chave que não existe
# print(dicionario_normal["chave_inexistente"])  # Isso levantaria um KeyError

# Exemplo com defaultdict
dicionario_padrao = defaultdict(int)  # O valor padrão para chaves inexistentes será 0

print("Valor para chave inexistente em defaultdict:\n", dicionario_padrao["chave_inexistente"])

# Adicionando valores ao defaultdict
dicionario_padrao["chave_existente"] = 10

print("Dicionário padrão após adição:\n", dicionario_padrao)

"""
Explicação:
- `defaultdict` é uma subclasse de `dict` que permite definir um valor padrão para chaves que não existem.
- No exemplo acima, usamos `defaultdict(int)`, o que significa que o valor padrão para chaves inexistentes será `0` (o valor padrão de `int()`).
- Isso evita erros ao acessar chaves que não foram previamente definidas e é útil em situações onde você quer garantir que todas as chaves tenham um valor inicial.
"""