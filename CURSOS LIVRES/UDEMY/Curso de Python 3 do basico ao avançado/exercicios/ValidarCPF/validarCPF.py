from time import sleep
import logging
import os
import re

# Configuração do logging
log_path = os.path.join('..','exercicios', 'ValidarCPF', 'logs', 'erros.log')
os.makedirs(os.path.dirname(log_path), exist_ok=True)
logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constantes
TAMANHO_CPF = 11
PESO_INICIAL = 10

# Funções auxiliares
def limpar_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))

def verificar_tamanho_cpf(cpf: str) -> bool:
    return len(cpf) == TAMANHO_CPF

def verificar_sequencia_repetida(cpf: str) -> bool:
    return cpf == cpf[0] * TAMANHO_CPF

def calcular_digito_verificador(cpf: str, tamanho: int) -> int:
    soma = sum(int(cpf[i]) * (tamanho + 1 - i) for i in range(tamanho))
    digito = 11 - (soma % 11)
    return digito if digito < 10 else 0

def validar_formato_cpf(cpf: str) -> bool:
    padrao = re.compile(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$')
    return bool(padrao.match(cpf))

# Função principal
def validar_cpf(cpf: str, debug: bool = False) -> tuple[bool, str]:
    try:
        cpf = limpar_cpf(cpf)
        if debug:
            print(f"CPF após remover os caracteres não numéricos: {cpf}")
            sleep(0.5)

        if not verificar_tamanho_cpf(cpf):
            return False, "CPF inválido: não tem 11 dígitos ou está vazio!"

        if verificar_sequencia_repetida(cpf):
            return False, "CPF inválido: sequência repetida."

        digito1 = calcular_digito_verificador(cpf, 9)
        digito2 = calcular_digito_verificador(cpf, 10)

        if debug:
            print(f"Primeiro dígito verificador calculado: {digito1}")
            print(f"Segundo dígito verificador calculado: {digito2}")
            sleep(0.5)

        if cpf[-2:] == f"{digito1}{digito2}":
            return True, "CPF válido."
        else:
            return False, "CPF inválido: dígitos verificadores incorretos."

    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        return False, "Erro durante a validação do CPF."

# Interação com o usuário
cpf_input = input("Digite um CPF (com pontos e traço, se desejar): ")
if not validar_formato_cpf(cpf_input):
    print("Formato de CPF inválido!")
else:
    valido, mensagem = validar_cpf(cpf_input, debug=True)
    print(mensagem)