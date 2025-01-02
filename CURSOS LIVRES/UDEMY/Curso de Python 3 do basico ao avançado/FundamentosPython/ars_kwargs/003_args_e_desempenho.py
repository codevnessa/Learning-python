"""
O uso de `*args` pode impactar o desempenho, especialmente quando se lida com um grande número de argumentos.
Isso ocorre porque `*args` cria uma tupla, e o processamento de tuplas pode ser mais lento em comparação com listas ou outros tipos de dados.
"""

def processar(*args):
    """
    Esta função recebe um número variável de argumentos usando `*args` e simula um processamento pesado.
    O tempo de execução pode aumentar significativamente com um grande número de argumentos.
    """
    for arg in args:
        # Simulação de processamento pesado
        pass

import time

inicio = time.time()
processar(*range(100000))
fim = time.time()
print(f"Tempo de execução: {fim - inicio} segundos")

"""
A função `processar` simula um processamento pesado com um grande número de argumentos.
O tempo de execução é medido para demonstrar o impacto de `*args` no desempenho.
"""