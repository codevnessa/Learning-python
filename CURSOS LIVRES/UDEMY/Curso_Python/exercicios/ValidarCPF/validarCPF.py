from time import sleep
import logging
import os
import re

# Configura o sistema de logging para registrar erros em um arquivo
log_path = os.path.join('..','exercicios', 'ValidarCPF', 'logs', 'erros.log')
os.makedirs(os.path.dirname(log_path), exist_ok=True)  # Cria o diretório de logs, se não existir
logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constantes
TAMANHO_CPF = 11  # Tamanho esperado de um CPF válido
PESO_INICIAL = 10  # Peso inicial para o cálculo dos dígitos verificadores

# Função para remover caracteres não numéricos do CPF
def limpar_cpf(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))

# Função para verificar se o CPF tem o tamanho correto
def verificar_tamanho_cpf(cpf: str) -> bool:
    return len(cpf) == TAMANHO_CPF

# Função para verificar se o CPF é uma sequência repetida (ex: 111.111.111-11)
def verificar_sequencia_repetida(cpf: str) -> bool:
    return cpf == cpf[0] * TAMANHO_CPF

# Função para calcular um dígito verificador do CPF
def calcular_digito_verificador(cpf: str, tamanho: int) -> int:
    soma = sum(int(cpf[i]) * (tamanho + 1 - i) for i in range(tamanho))  # Calcula a soma ponderada
    digito = 11 - (soma % 11)  # Calcula o dígito verificador
    return digito if digito < 10 else 0  # Retorna 0 se o dígito for 10 ou 11

# Função para validar o formato do CPF (com ou sem pontos e traço)
def validar_formato_cpf(cpf: str) -> bool:
    padrao = re.compile(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$')  # Regex para validar o formato
    return bool(padrao.match(cpf))

# Função principal para validar o CPF
def validar_cpf(cpf: str, debug: bool = False) -> tuple[bool, str]:
    try:
        cpf = limpar_cpf(cpf)  # Remove caracteres não numéricos
        if debug:
            print(f"CPF após remover os caracteres não numéricos: {cpf}")
            sleep(0.5)

        if not verificar_tamanho_cpf(cpf):  # Verifica se o CPF tem 11 dígitos
            return False, "CPF inválido: não tem 11 dígitos ou está vazio!"

        if verificar_sequencia_repetida(cpf):  # Verifica se o CPF é uma sequência repetida
            return False, "CPF inválido: sequência repetida."

        # Calcula os dois dígitos verificadores
        digito1 = calcular_digito_verificador(cpf, 9)
        digito2 = calcular_digito_verificador(cpf, 10)

        if debug:
            print(f"Primeiro dígito verificador calculado: {digito1}")
            print(f"Segundo dígito verificador calculado: {digito2}")
            sleep(0.5)

        # Verifica se os dígitos calculados coincidem com os do CPF
        if cpf[-2:] == f"{digito1}{digito2}":
            return True, "CPF válido."
        else:
            return False, "CPF inválido: dígitos verificadores incorretos."

    except Exception as e:
        logging.error(f"Erro inesperado: {e}")  # Registra erros inesperados no log
        return False, "Erro durante a validação do CPF."

# Interação com o usuário
cpf_input = input("Digite um CPF (com pontos e traço, se desejar): ")
if not validar_formato_cpf(cpf_input):  # Valida o formato do CPF antes de prosseguir
    print("Formato de CPF inválido!")
else:
    valido, mensagem = validar_cpf(cpf_input, debug=True)  # Valida o CPF
    print(mensagem)  # Exibe o resultado da validação