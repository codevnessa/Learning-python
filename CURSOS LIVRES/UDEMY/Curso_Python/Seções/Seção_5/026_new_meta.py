"""
Metaclasses são classes que definem o comportamento de outras classes. Aqui, a metaclasse `Meta` é usada para:
1. Adicionar um atributo (`attr`) a todas as classes que a utilizam.
2. Forçar a implementação de um método `falar`.
3. Validar se o atributo `nome` está presente nas instâncias das classes.
4. Adicionar um método `__repr__` personalizado.
"""

# Função para representação personalizada
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

# Metaclasse Meta
class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        # Cria a nova classe
        cls = super().__new__(mcs, name, bases, dct)
        # Adiciona um atributo à classe
        cls.attr = 1234
        # Adiciona a função `meu_repr` como método `__repr__` da classe
        cls.__repr__ = meu_repr

        # Verifica se o método `falar` está implementado
        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls

    def __call__(cls, *args, **kwargs):
        print('METACLASS CALL')
        # Cria a instância da classe
        instancia = super().__call__(*args, **kwargs)

        # Verifica se o atributo `nome` está presente na instância
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia

# Classe Pessoa que usa a metaclasse Meta
class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        # Cria a instância da classe
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        # self.nome = nome  # Comentado para simular a falta do atributo `nome`

    def falar(self):
        print('FALANDO...')

# Uso
try:
    p1 = Pessoa('Luiz')  # Tenta criar uma instância de Pessoa
    p1.falar()  # Chama o método `falar`
except NotImplementedError as e:
    print(f'Erro: {e}')  # Exibe o erro se o atributo `nome` não for criado

"""
- A metaclasse `Meta` controla a criação de classes que a utilizam.
- Ela adiciona um atributo `attr` e um método `__repr__` personalizado a todas as classes.
- A metaclasse verifica se o método `falar` está implementado e se o atributo `nome` está presente nas instâncias.
- Se alguma dessas condições não for atendida, uma exceção é lançada.
- A classe `Pessoa` usa a metaclasse `Meta`, mas o atributo `nome` está comentado no `__init__`, o que causa um erro ao tentar criar uma instância.
- Isso mostra como metaclasses podem ser usadas para impor regras e adicionar funcionalidades automaticamente às classes.
"""