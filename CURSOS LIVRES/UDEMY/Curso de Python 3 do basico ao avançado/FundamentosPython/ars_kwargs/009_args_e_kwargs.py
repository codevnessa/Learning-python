"""
`**kwargs` é usado para passar um número variável de argumentos nomeados para uma função.
Ele é frequentemente usado em conjunto com `*args`, que lida com argumentos posicionais.
`**kwargs` é um dicionário que contém os argumentos nomeados passados para a função.
"""

def exemplo_funcao(*args, **kwargs):
    """
    Esta função aceita um número variável de argumentos posicionais (`*args`) e argumentos nomeados (`**kwargs`).
    Ela imprime os argumentos posicionais e os argumentos nomeados separadamente.
    """
    print("Argumentos posicionais (*args):", args)
    print("Argumentos nomeados (**kwargs):", kwargs)

exemplo_funcao(1, 2, 3, nome="João", idade=30)

"""
A função `exemplo_funcao` usa `*args` para capturar argumentos posicionais e `**kwargs` para capturar argumentos nomeados.
Isso permite que a função seja extremamente flexível, aceitando qualquer combinação de argumentos posicionais e nomeados.
"""

"""
Argumentos posicionais (*args): (1, 2, 3)
Argumentos nomeados (**kwargs): {'nome': 'João', 'idade': 30}
"""

"""
- `*args` e `**kwargs` são convenções em Python, mas você pode usar outros nomes se preferir (por exemplo, `*params` e `**options`).
- `**kwargs` é útil quando você quer permitir que o usuário passe argumentos nomeados opcionais para uma função.
- A ordem dos parâmetros na definição da função deve ser: primeiro `*args`, depois `**kwargs`.
"""