# Variáveis livres + nonlocal (locals, globals)

# A função `globals()` retorna um dicionário com todas as variáveis globais do módulo atual.
# print(globals())  # Descomente para ver todas as variáveis globais

# Função externa que define uma variável livre (`valor_final`)
def concatenar(string_inicial):
    # `valor_final` é uma variável livre porque pertence ao escopo de `concatenar`,
    # mas será acessada e modificada pela função interna `interna`.
    valor_final = string_inicial

    # Função interna que usa a variável livre `valor_final`
    def interna(valor_a_concatenar=''):
        # `nonlocal` indica que `valor_final` não é local a `interna`,
        # mas pertence ao escopo da função externa (`concatenar`).
        nonlocal valor_final

        # Concatena o valor passado (`valor_a_concatenar`) à variável livre `valor_final`.
        valor_final += valor_a_concatenar

        # Retorna o valor atualizado de `valor_final`.
        return valor_final

    # Retorna a função interna `interna`, que "lembra" do escopo de `concatenar`.
    return interna


# Cria uma instância da função `interna` com o valor inicial 'a'.
c = concatenar('a')

# Chama a função `interna` com diferentes valores para concatenar.
print(c('b'))  # Saída: 'ab' (concatena 'b' ao valor inicial 'a')
print(c('c'))  # Saída: 'abc' (concatena 'c' ao valor atual 'ab')
print(c('d'))  # Saída: 'abcd' (concatena 'd' ao valor atual 'abc')

# Chama a função `interna` sem passar nenhum valor, retornando o valor atual de `valor_final`.
final = c()
print(final)  # Saída: 'abcd' (valor final após todas as concatenações)