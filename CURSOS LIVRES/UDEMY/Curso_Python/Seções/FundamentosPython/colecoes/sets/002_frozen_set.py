#  Demonstra como criar e usar um conjunto imutável (frozen set), que não pode ser alterado após a criação

# Criando um frozen set
cores = frozenset(["vermelho", "verde", "azul"])

# Tentando adicionar um item (isso causará um erro)
try:
    cores.add("amarelo")
except AttributeError as e:
    print(f"Erro: {e}")

# Exibindo o frozen set
print(cores)

"""
- cores = frozenset(["vermelho", "verde", "azul"]): Cria um frozen set com três cores.
- cores.add("amarelo"): Tenta adicionar "amarelo" ao frozen set, o que - causará um erro.
- print(cores): Exibe o frozen set.
"""