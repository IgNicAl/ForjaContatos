# ForjaContatos

ForjaContatos é um projeto de exemplo baseado em um diagrama UML para gerenciar contatos e jogos. Este projeto foi desenvolvido com foco na implementação de conceitos de Programação Orientada a Objetos (POO), utilizando Python. Ele apresenta um design modular que facilita a expansão e manutenção do código.

---

## Objetivo do Projeto

O principal objetivo do projeto é demonstrar a aplicação de conceitos de POO, como herança, composição, encapsulamento e polimorfismo. Além disso, o projeto busca fornecer uma interface interativa para gerenciar entidades como pessoas, jogos e estúdios de jogos, permitindo ao usuário realizar operações como cadastro, listagem e manipulação de dados.

---

## Estrutura do Projeto

### Diagrama UML

A estrutura segue o diagrama UML apresentado, com as seguintes relações:

- **Entidade (abstract):** Classe base para `Pessoa` e `Jogo`. Fornece atributos e métodos compartilhados.
- **Pessoa:** Composição com as classes `CPF` (para validação de CPF) e `Endereco` (para gerenciar endereços com CEP).
- **GameStudio:** Representa um estúdio de jogos que gerencia listas de pessoas e jogos.

### Hierarquia de Arquivos
```plaintext
ForjaContatos/
├── main.py         # Menu interativo principal
├── entidade.py     # Classe abstrata Entidade
├── cpf.py          # Classe CPF para validação de CPF
├── cep.py          # Classe CEP para consulta de endereços
├── endereco.py     # Classe Endereco que usa CEP
├── pessoa.py       # Classe Pessoa composta de CPF e Endereco
├── jogo.py         # Classe Jogo herdando de Entidade
├── gamestudio.py   # Classe GameStudio para gerenciar listas
└── .gitignore      # Arquivos e pastas a serem ignorados no Git
```

---

## Descrição das Classes

### `Entidade`
- Classe abstrata que serve como base para outras entidades.
- Atributos:
  - `nome` (str): Nome da entidade.
  - `ativo` (bool): Indica se a entidade está ativa.
- Métodos:
  - `exibir_info`: Método abstrato para exibir informações da entidade.
  - `atualizar_ativo`: Permite atualizar o estado ativo da entidade.

### `CPF`
- Classe para manipular e validar CPFs.
- Valida o CPF com base no algoritmo oficial de validação de dígitos verificadores.
- Formata o CPF para exibição no formato padrão brasileiro.

### `CEP`
- Classe para buscar e manipular informações de CEPs utilizando a API ViaCEP.
- Atributos incluem logradouro, bairro, cidade e estado.

### `Endereco`
- Classe que compõe informações detalhadas sobre endereços, integrando dados de CEP.
- Atributos:
  - `cep`: Instância da classe `CEP`.
  - `numero` (str): Número da residência.
  - `complemento` (str): Complemento do endereço.

### `Pessoa`
- Classe que representa uma pessoa física.
- Atributos:
  - `cpf`: Instância da classe `CPF`.
  - `endereco`: Instância da classe `Endereco`.
- Métodos:
  - `exibir_info`: Exibe informações detalhadas sobre a pessoa.

### `Jogo`
- Classe que representa um jogo.
- Atributos:
  - `descricao` (str): Descrição do jogo.
  - `genero` (str): Gênero do jogo.
  - `status` (str): Status atual do jogo (ex.: ativo, descontinuado).
- Métodos:
  - `exibir_info`: Retorna uma representação textual do jogo.

### `GameStudio`
- Classe para gerenciar um estúdio de jogos.
- Atributos:
  - `pessoas`: Lista de instâncias da classe `Pessoa`.
  - `jogos`: Lista de instâncias da classe `Jogo`.
- Métodos:
  - `adicionar_pessoa`: Adiciona uma nova pessoa ao estúdio.
  - `adicionar_jogo`: Adiciona um novo jogo ao estúdio.
  - `listar_pessoas`: Retorna uma lista com informações de todas as pessoas cadastradas.
  - `listar_jogos`: Retorna uma lista com informações de todos os jogos cadastrados.

---

## Configuração

### 1. Requisitos
Certifique-se de que possui os seguintes requisitos:
- Python 3.8+
- Biblioteca `requests` para buscas de CEP.

### 2. Configuração do Ambiente Virtual
1. No terminal, crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
2. Ative o ambiente:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```
3. Instale a dependência:
   ```bash
   pip install requests
   ```
4. Gere o arquivo `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

---

## Uso do Programa

1. Execute o programa principal:
   ```bash
   python main.py
   ```
2. Utilize o menu interativo para:
   - Adicionar pessoas.
   - Adicionar jogos.
   - Listar pessoas e jogos cadastrados.

### Exemplo de Entrada e Saída
#### Adicionando uma Pessoa
```plaintext
Menu Interativo:
1. Adicionar Pessoa
2. Adicionar Jogo
3. Listar Pessoas
4. Listar Jogos
5. Sair
Escolha uma opção: 1

Nome da pessoa: João
CPF da pessoa: 123.456.789-09
CEP: 50040090
Número: 123
Complemento: Apto 101
```
#### Resultado
```plaintext
Pessoa: João, CPF: 123.456.789-09, Endereco: Rua ABC, 123, Apto 101 - Bairro XYZ, Cidade/UF
```

---

