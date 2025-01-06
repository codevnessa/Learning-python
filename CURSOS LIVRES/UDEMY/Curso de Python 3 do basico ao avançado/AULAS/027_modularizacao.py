# Modularização - Entendendo os seus próprios módulos Python

# Quando você cria um arquivo Python, ele pode ser usado como um módulo.
# Um módulo é basicamente um arquivo com funções, classes ou variáveis que podem ser reutilizadas em outros arquivos.

# O primeiro módulo executado (o arquivo que você roda diretamente) chama-se __main__.
# Isso significa que, quando você executa um arquivo Python, o nome especial __name__ será "__main__".

# Você pode importar outro módulo inteiro ou apenas partes dele (funções, classes, variáveis).
# Para isso, use o comando `import` ou `from ... import ...`.

# O Python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Isso significa que, se você tiver outros módulos na mesma pasta ou em subpastas, o Python consegue encontrá-los.

# No entanto, o Python NÃO reconhece pastas e módulos acima do __main__ por padrão.
# Se você quiser importar algo de uma pasta acima, precisará ajustar o `sys.path` (mais sobre isso depois).

# O Python conhece todos os módulos e pacotes presentes nos caminhos de `sys.path`.
# `sys.path` é uma lista de diretórios onde o Python procura módulos e pacotes para importar.

# Importando o módulo "modulo"
# Aqui, estamos importando o módulo chamado "modulo" que está no mesmo diretório ou em um caminho conhecido pelo Python.
import modulo
from modulo import soma
#import sys
#sys.path.append('\home')
# Mostrando o nome deste módulo
# Como este é o arquivo principal que está sendo executado, o valor de __name__ será "__main__".
print('Este módulo se chama', __name__)

#print(*sys.path, sep='\n')
print(soma(3,5))