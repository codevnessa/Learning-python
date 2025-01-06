# Função que retorna um decorador. O decorador pode aceitar parâmetros externos.
# O decorador gerado também pode ter um parâmetro adicional, que é a função que será decorada.
def fabrica_de_decoradores(a=None, b=None, c=None):
    # A função 'fabrica_de_funcoes' é o decorador real, ele recebe a função original como parâmetro.
    def fabrica_de_funcoes(func):
        print('Decoradora 1')  # Mensagem indicando que a decoradora foi aplicada.
        
        # Função aninhada que irá envolver a função original.
        def aninhada(*args, **kwargs):
            # Aqui, mostramos os parâmetros passados para o decorador.
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')  # Mensagem que indica que a função foi chamada.
            
            # Executa a função original passando os argumentos recebidos.
            res = func(*args, **kwargs)
            return res  # Retorna o resultado da execução da função decorada.
        
        # Retorna a função aninhada, que agora contém o comportamento extra.
        return aninhada
    
    # Retorna o decorador com os parâmetros 'a', 'b' e 'c'.
    return fabrica_de_funcoes

# Aplicando o decorador que recebe parâmetros (1, 2, 3).
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y  # Função simples que soma dois números.

# Criando uma nova função decorada, sem passar parâmetros ao decorador.
decoradora = fabrica_de_decoradores()

# Aplicando um novo decorador a uma função lambda (multiplicação).
multiplica = decoradora(lambda x, y: x * y)

# Chamadas de função para ver os resultados.
dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)

# Imprime os resultados das funções decoradas.
print(dez_mais_cinco)  # Resultado da soma.
print(dez_vezes_cinco)  # Resultado da multiplicação.
