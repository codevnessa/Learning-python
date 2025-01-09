# Importando o módulo sys para acessar funções do sistema
import sys

# Criando um gerador que gera números de 0 a 99
generator = (n for n in range(100))  # Gerador: lazy evaluation (valores gerados sob demanda)
# Um gerador não armazena todos os valores na memória de uma vez. Ele gera cada valor apenas quando necessário.

# Criando uma lista que armazena números de 0 a 9
lista = [n for n in range(10)]  # Lista: armazena todos os valores na memória
# Uma lista armazena todos os seus elementos na memória de uma vez, o que pode consumir mais espaço.

# Verificando o tamanho em memória da lista e do gerador
print(sys.getsizeof(lista))  # Tamanho da lista em bytes
# sys.getsizeof() retorna o tamanho em bytes do objeto na memória.
# Listas consomem mais memória porque armazenam todos os elementos de uma vez.

print(sys.getsizeof(generator))  # Tamanho do gerador em bytes
# Geradores consomem menos memória porque não armazenam todos os valores de uma vez.
# Eles geram os valores sob demanda, um de cada vez.

# Iterando sobre o gerador e imprimindo seus valores
for n in generator:
    print(n)
# O loop for percorre o gerador, e a cada iteração, o próximo valor é gerado e impresso.
# Como o gerador usa lazy evaluation, ele só gera os valores quando necessário.

# Explicação dos conceitos:
# - Geradores: São eficientes em termos de memória porque geram valores sob demanda.
#   Eles são criados usando expressões geradoras (como (n for n in range(100))) ou funções com yield.
#
# - Listas: Armazenam todos os valores na memória de uma vez, o que pode ser ineficiente para grandes volumes de dados.
#
# - sys.getsizeof(): Retorna o tamanho em bytes de um objeto na memória.
#   Útil para comparar o consumo de memória entre diferentes tipos de objetos.
#
# No exemplo:
# - A lista [n for n in range(10)] armazena 10 números na memória.
# - O gerador (n for n in range(100)) não armazena os 100 números na memória; ele gera cada número sob demanda.
# - Por isso, o tamanho em memória do gerador é muito menor que o da lista, mesmo que o gerador possa produzir mais valores.