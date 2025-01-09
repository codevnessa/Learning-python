# Função que verifica se o denominador é zero
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')  # Lança uma exceção personalizada
    return True  # Retorna True se o denominador não for zero

# Função que verifica se o valor é int ou float
def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):  # Verifica se o tipo não é int ou float
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'  # Mensagem de erro detalhada
        )
    return True  # Retorna True se o valor for int ou float

# Função que realiza a divisão após validações
def divide(n, d):
    deve_ser_int_ou_float(n)  # Valida se n é int ou float
    deve_ser_int_ou_float(d)  # Valida se d é int ou float
    nao_aceito_zero(d)  # Valida se d não é zero
    return n / d  # Retorna o resultado da divisão