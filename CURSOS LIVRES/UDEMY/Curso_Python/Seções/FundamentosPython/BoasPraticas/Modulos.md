# Boas Práticas para Imports no Python

## Organize o Namespace

### `import nome_modulo`
- **Por que usar**: Mantém o namespace organizado, evitando conflitos de nomes e deixando claro de onde cada função ou classe veio.
  - **Exemplo**:
    ```python
    import math
    print(math.sqrt(16))  # Usa a função sqrt do módulo math
    ```

### `from nome_modulo import objeto`
- **Por que usar**: Importa apenas o necessário, evitando digitar o nome do módulo repetidamente.
  - **Exemplo**:
    ```python
    from math import sqrt
    print(sqrt(16))  # Não é necessário usar "math."
    ```

### Dê Apelidos (`as`)
- **Quando usar**: Ao trabalhar com módulos ou objetos com nomes longos para encurtar o código e melhorar a legibilidade.
  - **Exemplo**:
    ```python
    import numpy as np
    array = np.array([1, 2, 3])
    ```

## Organização

### Imports no Topo do Arquivo
- Mantenha todos os imports no início do arquivo.
- Separe os imports por categorias:
  1. Bibliotecas padrão.
  2. Bibliotecas de terceiros.
  3. Módulos locais.
  - **Exemplo**:
    ```python
    import os  # Biblioteca padrão
    import numpy as np  # Biblioteca de terceiros
    from .meu_modulo import minha_funcao  # Módulo local
    ```

### Imports Relativos para Módulos Locais
- Use imports relativos (., ..) para manter a estrutura de projetos grandes organizada.
  - **Exemplo**:
    ```python
    from .submodulo import minha_funcao
    ```

### Documentação de Imports Incomuns
- Adicione comentários para explicar imports que não são óbvios ou de uso comum.
  - **Exemplo**:
    ```python
    from functools import lru_cache  # Cache de resultados para otimização
    ```

## Prevenção de Conflitos

### Evite Conflitos de Nomes
- Escolha nomes de variáveis e funções que não coincidam com nomes de módulos ou funções importadas.
  - **Exemplo a evitar**:
    ```python
    import math
    math = 10  # Conflito com o módulo "math"
    ```

### Use `__all__`
- Em módulos personalizados, defina explicitamente o que deve ser acessível:
  - **Exemplo**:
    ```python
    __all__ = ['funcao1', 'Classe1']
    ```

---

# Más Práticas para Imports

### `from nome_modulo import *`
- **Evite**: Pode causar conflitos de nomes e dificultar a leitura do código.
  - **Exemplo a evitar**:
    ```python
    from math import *  # Não é claro de onde cada função veio
    print(sqrt(16))
    ```

### Conflitos de Nomes
- **Exemplo a evitar**: Criar uma variável chamada `list` sobrescreve a função built-in `list()` do Python.
  - **Exemplo**:
    ```python
    list = [1, 2, 3]  # Conflito com a função built-in "list"
    ```

### Imports Dentro de Funções ou Blocos de Código
- **Evite**: Dificulta a leitura e a manutenção do código, além de afetar o desempenho.
  - **Exemplo a evitar**:
    ```python
    def minha_funcao():
        import math  # Import dentro da função
        return math.sqrt(16)
    ```

### Ignorar Erros de Importação
- **Não use**: Blocos `try-except` para ignorar erros de importação. Corrija o problema.
  - **Exemplo a evitar**:
    ```python
    try:
        import modulo_inexistente
    except ImportError:
        pass  # Isso esconde o erro
    ```

### Nomes de Módulos Conflitantes
- **Evite**: Não crie módulos com nomes que conflitem com bibliotecas padrão ou de terceiros.
  - **Exemplo a evitar**:
    ```python
    # Arquivo chamado "math.py" conflita com o módulo padrão "math"
    ```

### Imports Desnecessários
- **Evite**: Aumenta o tempo de inicialização e consome mais memória.
  - **Exemplo a evitar**:
    ```python
    import os  # Import não utilizado no código
    ```

### Imports Circulares
- **Evite**: Quando dois módulos importam um ao outro, podem surgir erros difíceis de resolver.
  - **Exemplo a evitar**:
    ```python
    # modulo_a.py
    from modulo_b import funcao_b

    # modulo_b.py
    from modulo_a import funcao_a
    ```

### Imports Não Utilizados
- **Evite**: Remova imports que não estão sendo usados para evitar poluição e confusão no código.
  - **Exemplo**:
    ```python
    import math  # Não utilizado no código
    ```

---

# Dicas Gerais

### Mantenha o Código Limpo e Organizado
- Imports bem organizados facilitam a leitura e a manutenção.

### Use Ferramentas de Análise Estática
- Ferramentas como `flake8` ou `pylint` ajudam a identificar problemas com imports.

### Siga as Convenções da Comunidade
- Adote o estilo PEP 8 para manter boas práticas com imports.
