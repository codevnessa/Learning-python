# Criando Exceções Personalizadas
# Você pode criar suas próprias exceções personalizadas, definindo uma nova classe que herda de Exception.

# Sintaxe:
# class MinhaExcecao(Exception):
#     pass

# Exemplo:
class SaldoInsuficienteError(Exception):
    pass

saldo = 100
saque = int(input("Digite o valor do saque: "))

if saque > saldo:
    raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque!")
else:
    saldo -= saque
    print(f"Saque realizado com sucesso! Saldo atual: {saldo}")

# Explicação:
# O programa define uma exceção personalizada chamada SaldoInsuficienteError.
# Se o valor do saque for maior que o saldo, o programa levanta a exceção personalizada.
# Caso contrário, o saque é realizado e o saldo atual é exibido.