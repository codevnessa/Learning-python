# O Bloco else
# O bloco else pode ser usado em conjunto com try e except. Ele é executado apenas se não ocorrer nenhum erro no bloco try.

# Sintaxe:
# try:
#     # Código que pode gerar erros
# except:
#     # Tratamento de erros
# else:
#     # Código que será executado se não houver erros

# Exemplo:
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: você não digitou um número válido!")
else:
    print(f"O resultado da divisão é: {resultado}")

# Explicação:
# Se o usuário digitar um número válido (diferente de zero), o bloco else será executado e exibirá o resultado da divisão.
# Se ocorrer um erro, o bloco else será ignorado.