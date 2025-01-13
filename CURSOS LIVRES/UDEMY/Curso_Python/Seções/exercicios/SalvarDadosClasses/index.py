import json

# Caminho do arquivo JSON
CAMINHO_ARQUIVO = 'Curso_Python\\Seções\\Seção_5\\exercicios\\SalvarDadosClasses\\pessoas.json'

# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Função para salvar dados no arquivo JSON
def fazer_dump():
    pessoas = [
        {"nome": "João", "idade": 35},
        {"nome": "Maria", "idade": 25},
        {"nome": "Pedro", "idade": 40},
        {"nome": "Luiz", "idade": 20},
        {"nome": "Marcelo", "idade": 26},
        {"nome": "Luiza", "idade": 15},
    ]
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(pessoas, arquivo, indent=2)