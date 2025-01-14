# Use quando as partes são intrinsecamente ligadas ao todo e
# não têm existência independente, como no exemplo abaixo,
# onde a classe Cliente representa o 'todo' e a classe 
# Endereco representa as 'partes'. Os endereços estão 
# diretamente associados ao cliente e não fazem sentido 
# existir sem ele, a menos que sejam explicitamente criados 
# de forma independente. Isso significa que, quando o 
# cliente é apagado, os endereços criados dentro dele 
# também são apagados, mas os endereços criados fora do
# cliente continuam existindo.

# Classe que representa um cliente
class Cliente:
    def __init__(self, nome):
        self.nome = nome  # Nome do cliente
        self.enderecos = []  # Lista de endereços do cliente (começa vazia)

    # Adiciona um endereço criado diretamente dentro do cliente
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    # Adiciona um endereço que já foi criado fora do cliente
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    # Mostra a lista de endereços do cliente
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    # Método especial que é chamado quando o cliente é apagado
    def __del__(self):
        print('APAGANDO,', self.nome)


# Classe que representa um endereço
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua  # Nome da rua
        self.numero = numero  # Número do endereço

    # Método especial que é chamado quando o endereço é apagado
    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


# Cria um cliente chamado "Maria"
cliente1 = Cliente('Maria')

# Adiciona dois endereços diretamente ao cliente
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)

# Cria um endereço fora do cliente e o adiciona ao cliente
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)

# Mostra a lista de endereços do cliente
cliente1.listar_enderecos()

# Apaga o cliente (o que também apaga os endereços associados a ele)
del cliente1

# Mostra que o endereço externo ainda existe, pois foi criado fora do cliente
print(endereco_externo.rua, endereco_externo.numero)

# Mensagem para indicar o fim do código
print('######################## AQUI TERMINA MEU CÓDIGO')