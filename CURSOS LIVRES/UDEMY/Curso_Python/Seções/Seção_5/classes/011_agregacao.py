# Uso quando há uma relação de 'todo-parte', mas as partes
# podem existir independentemente do todo, como no exemplo
# abaixo, onde a classe Carrinho representa um 'todo' que 
# contém vários produtos (as 'partes'). Os produtos podem
# existir fora do carrinho, mas também podem ser adicionados
# a ele para formar uma compra.

# Classe que representa um carrinho de compras
class Carrinho:
    def __init__(self):
        self._produtos = []  # Lista de produtos no carrinho (começa vazia)

    # Calcula o total dos preços dos produtos no carrinho
    def total(self):
        return sum([p.preco for p in self._produtos])

    # Adiciona um ou mais produtos ao carrinho
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    # Mostra a lista de produtos no carrinho
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


# Classe que representa um produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome  # Nome do produto
        self.preco = preco  # Preço do produto


# Cria um carrinho de compras
carrinho = Carrinho()

# Cria dois produtos: uma caneta e uma camiseta
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

# Adiciona os produtos ao carrinho
carrinho.inserir_produtos(p1, p2)

# Mostra a lista de produtos no carrinho
carrinho.listar_produtos()

# Mostra o total da compra
print(carrinho.total())