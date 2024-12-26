# O que é o try e except?
# O bloco try e except é usado para tratar exceções (erros) em Python. Ele permite que você execute um código que pode gerar um erro, e caso esse erro ocorra, você pode tratá-lo de forma controlada, evitando que o programa pare abruptamente.

# Sintaxe básica:
# try:
#     # Código que pode gerar um erro
# except:
#     # Código que será executado caso ocorra um erro

# Exemplo básico:
try:
    print(10 / 0)  # Isso gera um erro (divisão por zero)
except:
    print("Ocorreu um erro!")

# Explicação:
# O código dentro do bloco try tenta executar a divisão 10 / 0.
# Como a divisão por zero é inválida, o Python gera uma exceção (ZeroDivisionError).
# O bloco except captura o erro e executa o código alternativo, exibindo a mensagem "Ocorreu um erro!".