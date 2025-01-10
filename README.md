# ForjaContatos

ForjaContatos é um projeto de exemplo baseado em um diagrama UML para gerenciar contatos e jogos. Ele utiliza classes abstratas, herança e composição para modelar entidades como pessoas, jogos e estúdios.

---

## Estrutura do Projeto

### Diagrama UML

A estrutura segue o diagrama UML apresentado, com as seguintes relações:

- **Entidade (abstract):** Classe base para `Pessoa` e `Jogo`.
- **Pessoa:** Composição com as classes `CPF` e `Endereco`.
- **GameStudio:** Contém listas de `Pessoa` e `Jogo`.

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

## Contribuindo
1. Faça um fork do repositório.
2. Crie uma branch para suas alterações:
   ```bash
   git checkout -b minha-alteracao
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Descrição do commit"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-alteracao
   ```
5. Abra um Pull Request no GitHub.

