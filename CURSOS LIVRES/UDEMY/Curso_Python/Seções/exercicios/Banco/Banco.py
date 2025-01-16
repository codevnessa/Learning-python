from abc import ABC, abstractmethod

# Classe Abstrata Conta
class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    @abstractmethod
    def sacar(self, valor):
        pass

# Classe ContaCorrente
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite=100):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    def sacar(self, valor):
        if valor > 0 and (self._saldo + self._limite) >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

# Classe ContaPoupanca
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

# Classe Abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

# Classe Cliente
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta

# Classe Banco
class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._clientes = []
        self._contas = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)
        self._contas.append(cliente.conta)

    def autenticar(self, cliente, agencia, numero_conta):
        if cliente in self._clientes:
            if cliente.conta.agencia == agencia and cliente.conta.numero_conta == numero_conta:
                return True
        return False

    def sacar(self, cliente, agencia, numero_conta, valor):
        if self.autenticar(cliente, agencia, numero_conta):
            cliente.conta.sacar(valor)
        else:
            print("Autenticação falhou. Saque não permitido.")

# Exemplo de uso
if __name__ == "__main__":
    # Criando contas
    conta_corrente = ContaCorrente("001", "12345-6", 1000)
    conta_poupanca = ContaPoupanca("001", "65432-1", 500)

    # Criando clientes
    cliente1 = Cliente("João", 30, conta_corrente)
    cliente2 = Cliente("Maria", 25, conta_poupanca)

    # Criando banco
    banco = Banco("Banco do Brasil")

    # Adicionando clientes ao banco
    banco.adicionar_cliente(cliente1)
    banco.adicionar_cliente(cliente2)

    # Realizando operações
    banco.sacar(cliente1, "001", "12345-6", 200)  # Saque bem-sucedido
    banco.sacar(cliente2, "001", "65432-1", 600)  # Saldo insuficiente
    banco.sacar(cliente1, "002", "12345-6", 100)  # Autenticação falhou

    # Depósitos
    cliente1.conta.depositar(300)
    cliente2.conta.depositar(200)