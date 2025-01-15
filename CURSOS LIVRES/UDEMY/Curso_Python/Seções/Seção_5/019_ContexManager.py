"""
O gerenciador de contexto em Python permite que você controle o ambiente de execução de um bloco de código ao implementar os métodos especiais __enter__ e __exit__ em uma classe. 

Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato.

O método __enter__ é chamado ao entrar no bloco with, enquanto o __exit__ é executado ao sair, recebendo informações sobre exceções ocorridas. Se __exit__ retornar True, as exceções serão suprimidas. Esse padrão é útil para liberar recursos automaticamente, como arquivos ou conexões de rede.
"""

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo  
        self._arquivo = None  
        print('INIT')

    def __enter__(self):
        print('ENTER RETURN')
        print('Abrindo arquivo....')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo  

    def __exit__(self, class_exception, exception_, traceback_):
        print('EXIT')
        print('Fechando arquivo.....')
        self._arquivo.close()  
        # Tratamento de exceções
        if class_exception is not None:  
            print(class_exception)  
            print(exception_)  
            print(traceback_) 
            exception_.add_note('Minha nota')  
            return True  

# Uso
instancia = MyOpen('019_contex.txt', 'w')  

with instancia as arquivo:  
    for i in range(1, 5): 
        arquivo.write('Linha' + str(i) + '\n')
    print('WITH', arquivo)  

"""
- A classe `MyOpen` é um gerenciador de contexto que abre e fecha arquivos de forma segura.
- O método `__enter__` é chamado ao entrar no bloco `with` e abre o arquivo.
- O método `__exit__` é chamado ao sair do bloco `with` e fecha o arquivo, garantindo que o recurso seja liberado.
- Se ocorrer uma exceção dentro do bloco `with`, o método `__exit__` pode tratá-la e adicionar informações úteis.
- O uso de `with` garante que o arquivo seja fechado corretamente, mesmo que ocorra um erro durante a execução.
"""