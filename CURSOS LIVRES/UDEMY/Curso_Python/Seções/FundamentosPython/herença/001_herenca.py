# A herança é como se uma classe "filha" pegasse características (atributos e métodos) de uma classe "pai".

# Classe base (pai)
class Animal:
    def __init__(self, nome):
        self.nome = nome  # Atributo comum a todos os animais

    def fazer_som(self):
        return "Som genérico de animal"  # Método genérico para fazer som
    
# Classe derivada (filha) que herda de Animal
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"  # Sobrescreve o método fazer_som para cachorros
    
class Gato(Animal):
    def fazer_som(self):
        return "MIAUUUUUUUUUUUUUUUUUUUUUUU"  # Sobrescreve o método fazer_som para gatos
    
# Criando um cachorro e um gato
meu_cachorro = Cachorro(nome="Rex")  # Instância de Cachorro
print(meu_cachorro.nome)  # Acessa o atributo nome herdado de Animal
print(meu_cachorro.fazer_som())  # Chama o método fazer_som sobrescrito

meu_gato = Gato(nome='Apolo')  # Instância de Gato
print(meu_gato.nome)  # Acessa o atributo nome herdado de Animal
print(meu_gato.fazer_som())  # Chama o método fazer_som sobrescrito

# Resumo:
# 1. Herança: A classe Cachorro e Gato herdam atributos e métodos da classe Animal, como o atributo 'nome'.
# 2. Sobrecarga de método: O método 'fazer_som' foi personalizado em cada classe filha (Cachorro e Gato).
# 3. Reutilização do código: A herança permite reutilizar código da classe Animal, evitando repetição.
# 4. Utilidade do conceito: A herança facilita a criação de classes mais específicas a partir de uma classe geral, promovendo organização e redução de redundância.