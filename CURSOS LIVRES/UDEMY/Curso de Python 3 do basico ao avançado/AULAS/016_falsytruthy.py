# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis: listas [], dicionários {}, conjuntos set()
# Imutáveis: tuplas (), strings "", números 0, 0.0, None, False, range(0)

# Definindo variáveis de diferentes tipos
lista = []          # Lista vazia (mutável)
dicionario = {}     # Dicionário vazio (mutável)
conjunto = set()    # Conjunto vazio (mutável)
tupla = ()          # Tupla vazia (imutável)
string = ''         # String vazia (imutável)
inteito = 0         # Inteiro zero (imutável)
flutuante = 0.0     # Float zero (imutável)
nada = None         # None (imutável)
falso = False       # Booleano False (imutável)
intervalo = range(0) # Range vazio (imutável)

# Função para verificar se um valor é falsy ou truthy
def falsy(valor):
    # Retorna 'falsy' se o valor for avaliado como False em um contexto booleano,
    # caso contrário, retorna 'truthy'
    return 'falsy' if not valor else 'truthy'

# Testando cada variável com a função falsy
print(f'TESTE', falsy('TESTE'))  # String não vazia é truthy
print(f'{lista=}', falsy(lista))  # Lista vazia é falsy
print(f'{dicionario=}', falsy(dicionario))  # Dicionário vazio é falsy
print(f'{conjunto=}', falsy(conjunto))  # Conjunto vazio é falsy
print(f'{tupla=}', falsy(tupla))  # Tupla vazia é falsy
print(f'{string=}', falsy(string))  # String vazia é falsy
print(f'{inteito=}', falsy(inteito))  # Inteiro zero é falsy
print(f'{flutuante=}', falsy(flutuante))  # Float zero é falsy
print(f'{nada=}', falsy(nada))  # None é falsy
print(f'{falso=}', falsy(falso))  # Booleano False é falsy
print(f'{intervalo=}', falsy(intervalo))  # Range vazio é falsy