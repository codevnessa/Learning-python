class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def exibir_informacoes(self):
        return f"Nome: {self.nome}\nSalário: R${self.salario:.2f}\nDepartamento: {self.departamento}"


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario, departamento)


if __name__ == "__main__":
    # Cadastro de Funcionário
    print("Cadastro de Funcionário")
    nome_funcionario = input("Digite o nome do funcionário: ")
    salario_funcionario = float(input("Digite o salário do funcionário: "))
    departamento_funcionario = input("Departamento: ")

    # Criando um objeto da classe Funcionario
    funcionario = Funcionario(nome_funcionario, salario_funcionario, departamento_funcionario)
    print(funcionario.exibir_informacoes())

    # Cadastro de Gerente
    print("\nCadastro do Gerente")
    nome_gerente = input("Digite o nome do gerente: ")
    salario_gerente = float(input("Digite o salário do gerente: "))
    departamento_gerente = input("Departamento: ")

    # Criando um objeto da classe Gerente
    gerente = Gerente(nome_gerente, salario_gerente, departamento_gerente)
    print(gerente.exibir_informacoes())