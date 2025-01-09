# Levantando Exceções Manualmente com raise
# Além de capturar exceções, você pode levantar exceções manualmente usando a palavra-chave raise. Isso é útil quando você quer forçar um erro em uma situação específica.

# Sintaxe:
# raise TipoDeErro("Mensagem de erro")

# Exemplo:
idade = int(input("Digite sua idade: "))

if idade < 0:
    raise ValueError("Idade não pode ser negativa!")

# Explicação:
# O programa pede ao usuário para digitar sua idade.
# Se o usuário digitar um número negativo, o programa levanta um ValueError com a mensagem "Idade não pode ser negativa!".