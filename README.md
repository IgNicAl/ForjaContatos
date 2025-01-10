# ForjaContatos

ForjaContatos é um projeto desenvolvido como parte das aulas de **Programação Orientada a Objetos (POO)** da turma 2024.2 do NExT, na **CESAR School**. O objetivo principal é consolidar os conceitos de POO por meio de uma aplicação prática e modular.

## 📂 Visão Geral
O projeto utiliza como base um **diagrama UML** que estrutura o gerenciamento de contatos e jogos. Com foco na implementação de princípios de POO, ele emprega **Python** para desenvolver um sistema modular que prioriza **expansão e manutenção de código**, promovendo boas práticas de desenvolvimento de software.

## 🛠️ Destaques do Projeto

- **Design Modular:** O sistema é organizado em módulos independentes que facilitam a manutenção e evolução do código.
- **Boas Práticas de Software:** Implementa conceitos como **separação de responsabilidades**, **abstração** e **reutilização de código**.
- **Gerenciamento de Entidades:** Oferece suporte ao gerenciamento de contatos e jogos, integrando diferentes entidades do sistema.
- **Persistência de Dados:** Inclui funcionalidades que permitem armazenar informações de forma eficiente.
- **Interface Gráfica:** Apresenta uma interface intuitiva, proporcionando uma experiência fluida para o usuário final.

---

## Índice

- [Objetivo do Projeto](#objetivo-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Status do Projeto](#status-do-projeto)
- [Acesso ao Projeto](#acesso-ao-projeto)
- [Pessoas Desenvolvedoras](#pessoas-desenvolvedoras-do-projeto)
- [Contribuições](#contribuições)

---

## Objetivo do Projeto

O principal objetivo do projeto é demonstrar a aplicação de conceitos de POO, como herança, composição, encapsulamento e polimorfismo. Além disso, o projeto busca fornecer uma interface interativa para gerenciar entidades como pessoas, jogos e estúdio de jogos, permitindo ao usuário realizar operações como cadastro, listagem e manipulação de dados.

---

## Funcionalidades

- **Gerenciamento de Pessoas:**
  - Adicionar pessoas ao sistema com informações como nome, CPF e endereço.
  - Listar todas as pessoas cadastradas.

- **Gerenciamento de Jogos:**
  - Adicionar jogos com nome, descrição, gênero e status.
  - Listar todos os jogos cadastrados.

- **Persistência de Dados:**
  - Salvar e carregar dados de pessoas e jogos em arquivos JSON.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas:**
  - `tkinter`: Utilizado para criar a interface gráfica do sistema. Permite a interação do usuário por meio de janelas e elementos visuais.
    - **Instalação:** `tkinter` é integrado ao Python e não requer instalação separada.
  - `requests`: Usado para consultar a API ViaCEP, buscando dados de endereço com base no CEP fornecido.
    - **Instalação:**
      ```bash
      pip install requests
      ```
  - `json`: Manipula dados para salvamento e leitura em arquivos JSON, garantindo persistência das informações.
    - **Instalação:** `json` é uma biblioteca padrão do Python.

---

## Como Executar

### Interface Gráfica

Para abrir a interface gráfica, execute:
```bash
python main.py --gui
```

### Menu Interativo

Para usar o menu interativo, execute:
```bash
python main.py
```

No menu interativo, você pode:
- Adicionar pessoas.
- Adicionar jogos.
- Listar pessoas ou jogos.
- Salvar ou carregar dados de arquivos JSON.

---

## Estrutura do Projeto

```plaintext
ForjaContatos/
├── app/
│   ├── cep.py          # Classe para manipulação de CEPs
│   ├── cpf.py          # Validação de CPFs
│   ├── endereco.py     # Classe para representação de endereços
│   ├── entidade.py     # Classe base abstrata para outras entidades
│   ├── gamestudio.py   # Classe principal para gerenciamento de estúdio de jogos
│   ├── interface.py    # Interface gráfica do sistema
│   ├── jogo.py         # Representação de um jogo
│   ├── pessoa.py       # Representação de uma pessoa
├── main.py             # Arquivo principal para execução do sistema
├── .gitignore          # Arquivos e pastas ignorados pelo Git
└── requirements.txt    # Dependências do projeto
```

---

## Status do Projeto

🚀 Em desenvolvimento. Algumas funcionalidades podem sofrer alterações ou melhorias nas próximas versões.

---

## Acesso ao Projeto

Para acessar os arquivos do projeto, clone o repositório:

```bash
git clone https://github.com/IgNicAl/ForjaContatos.git
```

---

## Pessoas Desenvolvedoras do Projeto

Este projeto foi desenvolvido por:

- [IgNicAl](https://github.com/IgNicAl)

---

## Contribuições

Contribuições são bem-vindas! Siga os seguintes passos:

1. Faça um fork do repositório.
2. Crie uma nova branch para sua contribuição:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Adiciona minha nova feature"
   ```
4. Faça o push para sua branch:
   ```bash
   git push origin minha-nova-feature
   ```
5. Abra um Pull Request.
