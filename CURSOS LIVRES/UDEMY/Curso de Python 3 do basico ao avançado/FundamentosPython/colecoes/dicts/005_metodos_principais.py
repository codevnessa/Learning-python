
#Métodos abordados:

# Criando um dicionário de exemplo
dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Método len(): Retorna a quantidade de chaves no dicionário.
quantidade_chaves = len(dicionario)
print("Quantidade de chaves no dicionário:", quantidade_chaves)
print()

# Método keys(): Retorna uma visão iterável com todas as chaves do dicionário.
print("Chaves do dicionário:", dicionario.keys())
print()

# Método values(): Retorna uma visão iterável com todos os valores do dicionário.
print("Valores do dicionário:", dicionario.values())
print()

# Método items(): Retorna uma visão iterável com pares chave-valor do dicionário.
print("Itens do dicionário:", dicionario.items())
print()

# Método get(): Retorna o valor de uma chave, ou um valor padrão se a chave não existir
print("Idade:", dicionario.get("idade", "Chave não encontrada"))
print("Profissão:", dicionario.get("profissao", "Chave não encontrada"))
print()

# Método update(): Atualiza o dicionário com os pares chave-valor de outro dicionário ou iterável
dicionario.update({"idade": 26, "profissao": "Engenheira"})
print("Dicionário após update:", dicionario)
print()

# Método pop(): Remove o item correspondente a uma chave e retorna o valor
idade = dicionario.pop("idade")
print("Idade removida:", idade)
print("Dicionário após pop:", dicionario)
print()

# Método popitem(): Remove e retorna o último par chave-valor adicionado ao dicionário
ultimo_item = dicionario.popitem()
print("Último item removido:", ultimo_item)
print("Dicionário após popitem:", dicionario)
print()

# Método clear(): Remove todos os itens do dicionário
dicionario.clear()
print("Dicionário após clear:", dicionario)
print()

# Método copy(): Retorna uma cópia superficial (shallow copy) do dicionário
dicionario = {"nome": "Alice", "idade": 25}
copia = dicionario.copy()
print("Cópia do dicionário:", copia)
print()

# Método fromkeys(): Cria um dicionário com chaves de um iterável e um valor padrão especificado
chaves = ["nome", "idade", "cidade"]
novo_dicionario = dict.fromkeys(chaves, "desconhecido")
print("Dicionário criado com fromkeys:", novo_dicionario)
print()

# Método setdefault():Retorna o valor de uma chave; insere a chave com um valor padrão se ela não existir.
idade = dicionario.setdefault("idade", 30)
profissao = dicionario.setdefault("profissao", "Engenheira")
print("Dicionário após setdefault:", dicionario)
print()

# Operador in: Verifica se uma chave existe no dicionário (operador)
if "nome" in dicionario:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")
print()

# Uso do del: Remove um item específico de uma chave ou o dicionário inteiro
del dicionario["idade"]
print("Dicionário após del:", dicionario)

"""
Explicação:
- `keys()`, `values()`, e `items()` retornam visões que refletem as mudanças no dicionário.
- `get()` é útil para acessar valores sem levantar erros se a chave não existir.
- `update()` pode ser usado para mesclar dicionários ou adicionar vários pares chave-valor de uma vez.
- `pop()` remove e retorna o valor associado a uma chave específica.
- `popitem()` remove e retorna o último par chave-valor adicionado ao dicionário.
- `clear()` remove todos os itens do dicionário.
- `copy()` cria uma cópia superficial do dicionário.
- `fromkeys()` cria um novo dicionário com chaves de um iterável e valores iguais a um valor especificado.
- `setdefault()` retorna o valor associado a uma chave, ou insere a chave com um valor padrão se ela não existir.
- `in` verifica se uma chave existe no dicionário.
- `del` remove um item específico de uma chave.
"""