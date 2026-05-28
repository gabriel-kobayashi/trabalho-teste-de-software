# Trabalho Final - Teste de Software

## Descrição

Aplicação web simples desenvolvida para a disciplina de Teste de Software.

O sistema possui dois fluxos principais:
- Login
- Formulário de contato

Foram desenvolvidos:
- Testes automatizados com Selenium WebDriver
- Testes unitários com Pytest
- Modelagem de testes utilizando tabelas de decisão

---

## Tecnologias utilizadas

- HTML
- CSS
- JavaScript
- Python
- Selenium
- Pytest

---

## Funcionalidades

### Login
- Validar login correto
- Validar login inválido
- Validar campos obrigatórios

### Contato
- Validar envio de mensagem
- Validar campos obrigatórios

---

## Estrutura do projeto

```txt
app/
tests/
```

---

## Como executar

### Instalar dependências

```bash
pip install selenium pytest webdriver-manager
```

### Executar testes

```bash
pytest
```

---

## Tipos de testes

### Caixa preta
Testes automatizados de interface utilizando Selenium.

### Caixa branca
Testes unitários utilizando Pytest.
