import enum

# Criando o enum com valores numéricos
direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA', 'CIMA', 'BAIXO'], start=1)

# Função para mover
def mover(direcao):
    if not isinstance(direcao, direcoes):
        raise ValueError('Direcao não encontrada!')

    print(f'Movendo para {direcao.name}')

# Exibindo as opções de direção com números
print("Escolha uma direção:")
for direcao in direcoes:
    print(f"{direcao.value}: {direcao.name}")

# Obtendo a entrada do usuário

try:
    entrada = int(input('Digite o número da direção: '))
    direcao_escolhida = direcoes(entrada)  # Converte o número em uma direção do enum
    mover(direcao_escolhida)
except ValueError:
    print('Entrada inválida! Certifique-se de digitar um número correspondente a uma direção.')

# Iterando sobre todas as direções possíveis
print("\nTodas as direções possíveis:")
for direcao in direcoes:
    print(f"{direcao.value}: {direcao.name}")