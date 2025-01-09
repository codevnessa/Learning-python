# O Que o Código Faz?

Esse código gera um CPF válido de forma **aleatória**. O CPF é aquele número que todo brasileiro tem, e ele precisa seguir algumas regrinhas para ser considerado válido. O código faz isso em várias etapas:

---

## ✨ Etapas do Código

### 1. **Gera os 9 Primeiros Dígitos**  
Primeiro, o código cria **9 números aleatórios** entre 0 e 9. Esses números formam os primeiros 9 dígitos do CPF, que podem ser qualquer combinação de números.

### 2. **Calcula os Dígitos Verificadores**  
Depois de gerar os 9 primeiros números, o código calcula os **2 dígitos verificadores**. Eles são super importantes porque garantem que o CPF seja válido, seguindo uma fórmula matemática específica.

- **1º Dígito Verificador**: Calculado com base nos 9 primeiros números.
- **2º Dígito Verificador**: Calculado com base nos 9 primeiros números + o 1º dígito verificador.

### 3. **Formata o CPF**  
No final, o código coloca os números no formato bonitinho que estamos acostumados a ver:  
**XXX.XXX.XXX-XX**. Ele coloca os **pontos** e o **traço** nos lugares certos para deixar o CPF mais legível.

---

## 🧐 Como Funciona Cada Parte?

### 1. **Geração dos 9 Primeiros Dígitos**  
O código usa uma função para gerar **9 números aleatórios** entre 0 e 9. Esses números formam os primeiros 9 dígitos do CPF.

### 2. **Cálculo dos Dígitos Verificadores**  
A fórmula matemática usa os 9 primeiros números para calcular os dois últimos dígitos do CPF. Isso garante que o CPF seja válido.

- O primeiro dígito verificador é calculado com base nos 9 primeiros números.
- O segundo dígito verificador é calculado com base nos 9 primeiros números + o primeiro dígito verificador.

### 3. **Formatação do CPF**  
Depois de gerar todos os 11 números, o código organiza tudo bonitinho no formato **XXX.XXX.XXX-XX**, colocando **pontos** e **traço** nos lugares corretos.

---

## 💡 Por Que Isso é Útil?

Esse código é bem útil quando você precisa de um **CPF válido para testes**. Pode ser usado em sistemas de cadastro ou qualquer aplicação que precise **validar CPFs**. Ele garante que o CPF gerado siga as regras oficiais e seja realista.
