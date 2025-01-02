# Define uma função chamada `cao` que recebe um argumento `latir` e retorna uma string formatada.
def cao(latir):
    return f'{latir}'

# Define uma função chamada `executa_som` que recebe uma função `latido` e argumentos variáveis (*args).
# Essa função executa a função `latido` passando os argumentos recebidos.
def executa_som(latido, *args):
    return latido(*args)

# Chama a função `executa_som`, passando a função `cao` como argumento e uma string concatenada.
print(
    executa_som(cao, 'AUUUUUUUUUUUUUUUUUU\n' 'AUAUAUA\n' 'AUUUUUUUUUUUUUUUUUU' )
)