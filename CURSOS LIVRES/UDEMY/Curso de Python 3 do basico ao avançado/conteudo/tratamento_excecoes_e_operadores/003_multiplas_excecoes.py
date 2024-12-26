# Tratando Múltiplas Exceções
# Você pode tratar diferentes tipos de exceções de forma separada, usando múltiplos blocos except. Isso permite que você forneça tratamentos específicos para cada tipo de erro.

# Sintaxe:
# try:
#     # Código que pode gerar erros
# except TipoDeErro1:
#     # Tratamento para TipoDeErro1
# except TipoDeErro2:
#     # Tratamento para TipoDeErro2
# except:
#     # Tratamento para qualquer outro erro

# Exemplo:
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: você não digitou um número válido!")
except:
    print("Ocorreu um erro desconhecido!")

# Explicação:
# O programa pede ao usuário para digitar um número.
# Se o usuário digitar 0, ocorre um ZeroDivisionError.
# Se o usuário digitar algo que não seja um número, ocorre um ValueError.
# Se ocorrer qualquer outro erro, o último bloco except captura e trata o erro.