# Cria e manipula um conjunto básico em Python, adicionando e removendo elementos

# Criando um conjunto
frutas = {"maçã", "banana", "laranja"}

# Adicionando um item ao conjunto
frutas.add("uva")

# Removendo um item do conjunto
frutas.remove("banana")

# Verificando se um item está no conjunto
if "maçã" in frutas:
    print("Maçã está no conjunto!")

# Exibindo o conjunto
print(frutas)

"""
- frutas = {"maçã", "banana", "laranja"}: Cria um conjunto com três frutas.
- frutas.add("uva"): Adiciona "uva" ao conjunto.
- frutas.remove("banana"): Remove "banana" do conjunto.
- if "maçã" in frutas:: Verifica se "maçã" está no conjunto.
- print(frutas): Exibe o conjunto atualizado.
"""