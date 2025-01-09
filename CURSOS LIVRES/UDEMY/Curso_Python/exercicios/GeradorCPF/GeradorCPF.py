import random

def gerar_numeros_aleatorios() -> str:
    """
    Gera os 9 primeiros dígitos do CPF de forma aleatória.
    """
    return ''.join([str(random.randint(0, 9)) for _ in range(9)])

def calcular_digito_verificador(cpf_parcial: str, peso_inicial: int) -> int:
    """
    Calcula um dígito verificador para o CPF.
    """
    total = sum(int(cpf_parcial[i]) * (peso_inicial - i) for i in range(len(cpf_parcial)))
    digito = 11 - (total % 11)
    return digito if digito < 10 else 0

def calcular_digitos_verificadores(cpf_parcial: str) -> str:
    """
    Calcula os dois dígitos verificadores do CPF.
    """
    # Calcula o primeiro dígito verificador (peso inicial = 10)
    digito1 = calcular_digito_verificador(cpf_parcial, 10)
    # Adiciona o primeiro dígito ao CPF parcial e calcula o segundo dígito (peso inicial = 11)
    digito2 = calcular_digito_verificador(cpf_parcial + str(digito1), 11)
    return f"{digito1}{digito2}"

def formatar_cpf(cpf: str) -> str:
    """
    Formata o CPF no padrão XXX.XXX.XXX-XX.
    """
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def gerar_cpf() -> str:
    """
    Gera um CPF válido e formatado.
    """
    # Gera os 9 primeiros dígitos
    cpf_parcial = gerar_numeros_aleatorios()
    # Calcula os dígitos verificadores
    digitos_verificadores = calcular_digitos_verificadores(cpf_parcial)
    # Combina os dígitos parciais com os verificadores
    cpf_completo = cpf_parcial + digitos_verificadores
    # Formata o CPF
    return formatar_cpf(cpf_completo)

# Exemplo de uso
if __name__ == "__main__":
    cpf_gerado = gerar_cpf()
    print(f"CPF gerado: {cpf_gerado}")