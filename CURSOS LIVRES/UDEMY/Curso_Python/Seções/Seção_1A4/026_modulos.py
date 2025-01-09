# Importando o módulo inteiro (a "caixa de ferramentas" chamada sys)
import sys

# Criando uma variável chamada "platform" com o valor 'A MINHA'
platform = 'A MINHA'

# Usando a ferramenta "platform" que está dentro da caixa "sys"
# Isso vai mostrar o sistema operacional que você está usando (por exemplo, Windows, Linux, etc.)
print(sys.platform)

# Mostrando a variável "platform" que eu criei, não a do módulo sys
print(platform)

# Agora, vamos ver outras formas de pegar ferramentas da caixa:

# 1. Pegando ferramentas específicas da caixa (sem trazer a caixa inteira)
# from sys import exit, platform
# Isso permite usar "platform" e "exit" diretamente, sem precisar escrever "sys." antes.

# 2. Dando um apelido para a caixa de ferramentas
# import sys as s
# Agora, em vez de escrever "sys.", você pode escrever "s." para acessar as ferramentas.

# 3. Dando um apelido para uma ferramenta específica
# from sys import platform as pf
# Agora, você pode usar "pf" em vez de "platform" para se referir à ferramenta.

# 4. Importando tudo de uma vez (não é recomendado!)
# from sys import *
# Isso traz todas as ferramentas da caixa "sys" de uma vez, mas pode causar confusão,
# porque você não sabe de onde veio cada ferramenta.

# Exemplo de uso do alias (apelido) para a ferramenta "platform":
# from sys import platform as pf
# print(pf)  # Isso vai mostrar o sistema operacional, mas usando o apelido "pf"

# Exemplo de uso do alias para a caixa inteira:
# import sys as s
# print(s.platform)  # Acessando a ferramenta "platform" usando o apelido "s"

# Lembre-se: escolha a forma que fizer mais sentido para o seu código!
# Se você quiser evitar confusão, é melhor usar "import nome_modulo" ou "from nome_modulo import objeto".