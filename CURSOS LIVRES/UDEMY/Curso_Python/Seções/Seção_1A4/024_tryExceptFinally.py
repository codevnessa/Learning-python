try:
    print('ABRIR ARQUIVO')  # Simula a abertura de um arquivo
    8 / 0  # Causa um ZeroDivisionError (divisão por zero)
except ZeroDivisionError as e:
    print(e.__class__.__name__)  # Nome da classe da exceção: "ZeroDivisionError"
    print(e)  # Mensagem de erro: "division by zero"
    print('DIVIDIU ZERO')  # Mensagem personalizada para divisão por zero
except IndexError as error:
    print('IndexError')  # Captura erros de índice (não é acionado neste caso)
except (NameError, ImportError):
    print('NameError, ImportError')  # Captura NameError e ImportError (não é acionado)
else:
    print('Não deu erro')  # Executado se nenhum erro ocorrer no bloco try
finally:
    print('FECHAR ARQUIVO')  # Sempre executado, independentemente de erros