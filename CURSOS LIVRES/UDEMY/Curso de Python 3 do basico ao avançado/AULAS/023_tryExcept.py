try:
    a = 18
    b = 0
    # print(b[0])  # Isso causaria um TypeError (b não é iterável)
    # print('Linha 1'[1000])  # Isso causaria um IndexError (índice fora do range)
    c = a / b  # Isso causa um ZeroDivisionError (divisão por zero)
    print('Linha 2')  # Esta linha não será executada devido ao erro anterior
except ZeroDivisionError as e:
    print(e.__class__.__name__)  # Nome da classe da exceção: "ZeroDivisionError"
    print(e)  # Mensagem de erro: "division by zero"
except NameError:
    print('Nome b não está definido')  # Captura erros de variáveis não definidas
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')  # Captura TypeError e IndexError
    print('MSG:', error)  # Mensagem de erro
    print('Nome:', error.__class__.__name__)  # Nome da classe da exceção
except Exception:
    print('ERRO DESCONHECIDO.')  # Captura qualquer outra exceção não tratada

print('CONTINUAR')  # Executa após o bloco try-except