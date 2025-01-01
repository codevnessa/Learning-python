# Gerando um CPF Válido

## 1. Parte 1: Gerar Números Aleatórios

### Pra que?
Gera os **9 primeiros números** do CPF de forma aleatória.

### Como Funciona?
Cria uma sequência de 9 números, onde cada número pode ser de 0 a 9. Por exemplo: `123456789`.

---

## 2. Parte 2: Calcular o Dígito Verificador

### Pra que?
Calcula os **dois últimos números** do CPF, conhecidos como **dígitos verificadores**, que validam se o CPF é real.

### Como Funciona?
Usa os 9 números gerados anteriormente e realiza um cálculo matemático com uma fórmula específica definida pelo governo brasileiro para calcular os dois últimos dígitos.

---

## 3. Parte 3: Formatar o CPF

### Pra que?
Formata o CPF para o formato que estamos acostumados a ver, com pontos e traço.

### Como Funciona?
Usa os 11 números do CPF (9 primeiros + 2 verificadores) e organiza da seguinte maneira: `XXX.XXX.XXX-XX`. Exemplo: `123.456.789-09`.

---

## 4. Parte 4: Juntar Tudo e Gerar o CPF

### Pra que?
Combina todas as etapas anteriores para gerar um **CPF válido e formatado**.

### Como Funciona?
Chama as funções nas ordens corretas:
1. Gera os 9 primeiros números.
2. Calcula os 2 dígitos verificadores.
3. Formata o CPF.

No final, retorna um CPF completo, como: `123.456.789-09`.

---

## Por Que Separar em Partes?

### Vantagens:
- **Entendimento**: Cada parte faz uma coisa só, facilitando o entendimento do processo.
- **Reutilização**: Possibilidade de usar partes separadas, como gerar apenas os dígitos verificadores ou formatar um CPF.
- **Manutenção**: Se algo der errado, fica mais fácil identificar onde está o problema.

---

## Exemplo de Como Funciona

Imagine o código como uma **fábrica de CPFs**:
- A **primeira máquina** gera os 9 primeiros números.
- A **segunda máquina** calcula os 2 últimos números.
- A **terceira máquina** formata os números corretamente.

No final, você tem um CPF válido e pronto para uso.

---

## Resumo

O código faz o seguinte:
1. Gera os **9 primeiros números** do CPF.
2. Calcula os **2 últimos números** que validam o CPF.
3. Formata o CPF com **pontos** e **traço**.
4. Junta tudo e entrega um **CPF válido**.
