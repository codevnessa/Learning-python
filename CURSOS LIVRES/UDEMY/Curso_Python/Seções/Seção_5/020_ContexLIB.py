from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo,modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo,modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu um erro inesperado', e)
    finally:   
        print('Fechando Arquivo')
    
with my_open('020_LIB.txt', 'w') as arquivo:
    for i in range (1,6):
        arquivo.write('Linha' + str(i) + '\n', 123)
        