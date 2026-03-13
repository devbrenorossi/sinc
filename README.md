# 📦 Sinc - Sistema de Controle de Estoque

Sinc é um sistema simples de **gerenciamento de estoque via terminal (CLI)** desenvolvido em Python.
O programa permite cadastrar, listar, atualizar e remover produtos, armazenando os dados em um arquivo JSON.

Este projeto foi criado com o objetivo de **praticar lógica de programação, manipulação de arquivos e organização de código em módulos**.

---

## 🚀 Funcionalidades

* ➕ Cadastrar produtos
* 📋 Listar produtos cadastrados
* ✏️ Atualizar informações de produtos
* ❌ Remover produtos do estoque
* 💾 Persistência de dados usando arquivo JSON
* 🔢 Geração automática de ID para cada produto

---

## 🗂 Estrutura do Projeto

```id="8vm7qb"
Sinc/
│
├── main.py
├── database.py
├── ESTOQUE.json
│
└── modulos/
    ├── functions.py
    └── utils.py
```

### Descrição dos arquivos

| Arquivo        | Função                                     |
| -------------- | ------------------------------------------ |
| `main.py`      | Controla o menu e a execução do programa   |
| `database.py`  | Responsável por carregar e salvar os dados |
| `functions.py` | Implementa as operações de CRUD            |
| `utils.py`     | Funções auxiliares da interface            |
| `ESTOQUE.json` | Armazena os dados do estoque               |

---

## 🧠 Estrutura dos Dados

Os dados são armazenados em JSON no seguinte formato:

```json id="42zrl5"
{
  "proximo_id": 3,
  "produtos": {
    "1": {
      "nome": "ARROZ",
      "quantidade": 10
    },
    "2": {
      "nome": "FEIJAO",
      "quantidade": 5
    }
  }
}
```

---

## ▶️ Como executar

Clone o repositório:

```id="4n3v1s"
git clone https://github.com/devbrenorossi/Sinc.git
```

Entre na pasta do projeto:

```id="uxcnd7"
cd Sinc
```

Execute o programa:

```id="d8ewl2"
python main.py
```

---

## 🛠 Tecnologias utilizadas

* Python
* JSON
* Terminal / CLI

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

* Estruturas de dados em Python
* Manipulação de arquivos
* Organização de código em módulos
* Desenvolvimento de aplicações em linha de comando

---

## 🔮 Possíveis melhorias

* 🔎 Buscar produtos pelo nome
* 📊 Ordenar produtos por quantidade
* ⚠️ Alerta de estoque baixo
* 📁 Exportar estoque para CSV
* 🗄 Substituir JSON por banco de dados (SQLite)

---

## 👨‍💻 Autor

**Breno Rossi**
