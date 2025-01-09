# Boas Práticas de Modularização

### Divida o código em módulos com responsabilidades claras
- **Por que fazer**: Facilita a manutenção, a leitura e a reutilização do código.
- **Exemplo**:
  ```python
  # módulo para manipulação de arquivos
  # arquivo: manipulador_arquivos.py
  def ler_arquivo(caminho):
      with open(caminho, 'r') as f:
          return f.read()

  # módulo para cálculos matemáticos
  # arquivo: calculos.py
  def somar(a, b):
      return a + b
  ```

### Use nomes descritivos para módulos e funções
- **Por que fazer**: Ajuda a entender rapidamente o propósito do módulo.
- **Exemplo**:
  - `calculadora.py` para funções matemáticas.
  - `logger.py` para registro de logs.

### Organize módulos em pacotes (pastas com `__init__.py`)
- **Por que fazer**: Estrutura melhor projetos grandes.
- **Exemplo**:
  ```plaintext
  utils/
  ├── __init__.py
  ├── logger.py
  └── validators.py
  ```

### Use `if __name__ == "__main__":` para código executável
- **Por que fazer**: Evita que o código seja executado ao importar o módulo.
- **Exemplo**:
  ```python
  # arquivo: exemplo.py
  def saudacao():
      print("Olá, mundo!")

  if __name__ == "__main__":
      saudacao()
  ```

### Documente seus módulos e funções
- **Por que fazer**: Facilita a colaboração e o uso do código.
- **Exemplo**:
  ```python
  """Módulo de cálculos matemáticos.

  Contém funções para operações básicas como soma, subtração, etc.
  """

  def somar(a, b):
      """Retorna a soma de dois números."""
      return a + b
  ```

### Evite dependências circulares
- **Por que evitar**: Previne erros difíceis de depurar.
- **Exemplo**:
  ```python
  # Em vez de:
  # módulo_a.py importa módulo_b
  # módulo_b.py importa módulo_a

  # Use:
  # módulo_comum.py contém funções compartilhadas por ambos.
  ```

### Use imports relativos para projetos grandes
- **Por que fazer**: Facilita a organização e reduz erros.
- **Exemplo**:
  ```python
  # arquivo: utils/logger.py
  from .validators import validar_email
  ```

## Mantenha os imports no topo do arquivo
- **Por que fazer**: Melhor organização e legibilidade.
- **Exemplo**:
  ```python
  # Imports no topo
  import os
  import sys
  from utils import logger
  ```

### Use `__all__` para controlar o que é exportado
- **Por que fazer**: Limita o que será acessível ao importar tudo do módulo.
- **Exemplo**:
  ```python
  __all__ = ['funcao_principal', 'ClassePrincipal']
  ```

### Teste seus módulos de forma independente
- **Por que fazer**: Garante que cada módulo funcione antes da integração.
- **Exemplo**:
  ```bash
  python -m unittest testes/teste_modulo.py
  ```

---

# Más Práticas de Modularização

## Criar módulos muito grandes ou com muitas responsabilidades
- **Por que evitar**: Difícil de entender e manter.
- **Exemplo a evitar**:
  ```python
  # Um único módulo com várias funções não relacionadas
  def somar(a, b): ...
  def validar_email(email): ...
  def registrar_log(mensagem): ...
  ```

### Usar nomes genéricos ou confusos para módulos
- **Por que evitar**: Nomes como `utils.py` não são claros.
- **Exemplo a evitar**:
  ```plaintext
  # Evite isso:
  utils.py
  ```
  - **Prefira**: Nomes como `calculadora.py` ou `validador.py`.

### Não usar `if __name__ == "__main__":`
- **Por que evitar**: Código executável será rodado ao importar o módulo.
- **Exemplo a evitar**:
  ```python
  print("Executando módulo")  # Isso será executado ao importar
  ```

#### Criar dependências desnecessárias entre módulos
- **Por que evitar**: Dificulta a reutilização.
- **Exemplo a evitar**:
  ```python
  # Importar módulos que não são usados
  import os
  ```

### Não documentar módulos e funções
- **Por que evitar**: Difícil de usar e colaborar.
- **Exemplo a evitar**:
  ```python
  # Sem docstrings
  def somar(a, b):
      return a + b
  ```

### Usar imports circulares
- **Por que evitar**: Pode causar erros imprevisíveis.

### Importar tudo com `from modulo import *`
- **Por que evitar**: Polui o namespace e pode causar conflitos.
- **Exemplo a evitar**:
  ```python
  from math import *
  ```

### Não organizar imports
- **Por que evitar**: Dificulta a leitura.

### Ignorar erros de importação
- **Por que evitar**: Pode esconder problemas reais.
- **Exemplo a evitar**:
  ```python
  try:
      import modulo_inexistente
  except ImportError:
      pass
  ```

### Não testar módulos de forma independente
- **Por que evitar**: Integração pode falhar sem testes prévios.

---

## Dicas Gerais para Modularização

### Mantenha o código DRY (Don't Repeat Yourself)
- Se copiar e colar código, é hora de modularizá-lo.

### Siga o princípio KISS (Keep It Simple, Stupid)
- Prefira módulos simples e diretos.

### Use ferramentas de análise estática
- Ferramentas como `flake8`, `pylint` ou `black` ajudam na qualidade do código.

### Siga as convenções da comunidade
- Adote o estilo PEP 8 para modularização e organização de imports.
