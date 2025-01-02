# Definindo uma função externa que retorna uma função interna
def criar_contador():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

# Criando uma instância da closure
contador = criar_contador()

# Usando a closure para incrementar o contador
print(contador())  # 1
print(contador())  # 2

"""
Explicação do código:
1. A função `criar_contador` é definida para inicializar uma variável `contador` com 0.
2. A função interna `incrementar` é definida para incrementar `contador` e retornar seu valor.
3. A função `incrementar` é retornada pela função `criar_contador`.
4. Uma instância da closure é criada e armazenada na variável `contador`.
5. A closure é chamada duas vezes, incrementando e retornando o valor de `contador` a cada chamada.
6. Os resultados são impressos, mostrando 1 e 2.

Isso demonstra como closures podem capturar e reter variáveis do escopo em que foram definidas.
"""