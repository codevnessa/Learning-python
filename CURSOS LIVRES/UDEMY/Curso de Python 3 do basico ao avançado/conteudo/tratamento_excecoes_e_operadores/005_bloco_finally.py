# O Bloco finally
# O bloco finally é executado independentemente de ocorrer um erro ou não. Ele é usado para código que deve ser executado sempre, como fechar um arquivo ou liberar recursos.

# Sintaxe:
# try:
#     # Código que pode gerar erros
# except:
#     # Tratamento de erros
# finally:
#     # Código que será executado sempre

# Exemplo:
try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: o arquivo não foi encontrado!")
finally:
    print("Fechando o arquivo...")
    arquivo.close()

# Explicação:
# O programa tenta abrir um arquivo chamado arquivo.txt.
# Se o arquivo não existir, ocorre um FileNotFoundError, e o bloco except trata o erro.
# Independentemente de ocorrer um erro ou não, o bloco finally será executado, fechando o arquivo.