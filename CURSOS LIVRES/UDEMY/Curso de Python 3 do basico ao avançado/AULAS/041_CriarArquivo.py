caminho_arquivo = r'C:\\#FUTURO\\GITHUB\\learning\\Learning_python\\CURSOS LIVRES\\UDEMY\Curso de Python 3 do basico ao avançado\\AULAS'
caminho_arquivo += '\\041_ArquvoCriado.md'

# Primeiro bloco: Cria o arquivo e escreve conteúdo inicial
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Olá mundo\n')  # Escreve no arquivo
    arquivo.write('Arquivo vai ser fechado\n')  # Escreve no arquivo

# Segundo bloco: Reabre o arquivo em modo 'w+' (escrita e leitura)
with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('# Linha 1\n')  
    arquivo.write('# Linha 2\n')  
    arquivo.writelines(('# Linha 3\n', '# Linha 4\n'))

    arquivo.seek(0, 0)  # Retorna o cursor 
    print(arquivo.read())  
    print('# Lendo')  

    arquivo.seek(0, 0)  # Retorna o cursor 
    print(arquivo.readline(), end='') 
    print(arquivo.readline().strip())  
    print(arquivo.readline().strip())  
    print('# READLINES') 
    arquivo.seek(0, 0)  # Retorna o cursor
    for linha in arquivo.readlines():  
        print(linha.strip()) 

print('#' * 10)  

# Terceiro bloco: Reabre o arquivo em modo 'r' (leitura)
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())  