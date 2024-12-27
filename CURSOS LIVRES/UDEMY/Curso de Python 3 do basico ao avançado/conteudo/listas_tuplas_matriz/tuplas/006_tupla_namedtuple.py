# Explicação do conteúdo: namedtuple é uma função da biblioteca collections que cria tuplas com campos nomeados.
# Isso torna o código mais legível e organizado.

# Exemplo de uso de namedtuple:
from collections import namedtuple

Pessoa = namedtuple("Pessoa", ["nome", "idade"])  # Define uma namedtuple
pessoa = Pessoa(nome="Maria", idade=30)  # Cria uma instância da namedtuple
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)

# Explicação do código:
# 1. A namedtuple Pessoa é criada com os campos "nome" e "idade".
# 2. Uma instância da namedtuple é criada com valores específicos.
# OBS: namedtuple combina a imutabilidade das tuplas com a legibilidade de campos nomeados.