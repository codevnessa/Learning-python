try:
    a = 18
    b = 0
    # print(b[0])  # Isso causaria um TypeError (b não é iterável)
    print('Linha 1'[1000])  # Isso causa um IndexError (índice fora do range)
    c = a / b  # Isso causaria um ZeroDivisionError (divisão por zero)
    print('Linha 2')  # Esta linha não será executada devido ao erro anterior
except ZeroDivisionError:
    print('Dividiu por zero.')  # Captura divisão por zero
except NameError:
    print('Nome b não está definido')  # Captura variáveis não definidas
except (TypeError, IndexError):
    print('TypeError + IndexError')  # Captura TypeError e IndexError juntos
except Exception:
    print('ERRO DESCONHECIDO.')  # Captura qualquer outra exceção não tratada

print('CONTINUAR')  # Executa após o bloco try-except

