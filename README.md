# Sistema de Gestão Acadêmica (Console)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-green.svg)]()
[![Licença](https://img.shields.io/badge/Licença-MIT-lightgrey.svg)](LICENSE)

## 📝 Descrição do Projeto

Este projeto é um sistema de gestão acadêmica básico, desenvolvido em Python, com interface de console. Ele simula o gerenciamento de dados essenciais para uma instituição de ensino, permitindo a realização de operações CRUD (Create, Read, Update, Delete) em diferentes entidades.

Foi concebido como uma atividade prática para solidificar os fundamentos da programação em Python e a manipulação de dados em arquivos.

## ✨ Funcionalidades

O sistema oferece um menu interativo que permite ao usuário:

* **Gerenciar Estudantes:** Adicionar, listar, atualizar e excluir registros de estudantes.
* **Gerenciar Professores:** Adicionar, listar, atualizar e excluir registros de professores.
* **Gerenciar Disciplinas:** Adicionar, listar, atualizar e excluir registros de disciplinas.
* **Gerenciar Turmas:** Adicionar, listar, atualizar e excluir registros de turmas (vinculando professores e disciplinas).
* **Gerenciar Matrículas:** Adicionar, listar, atualizar e excluir registros de matrículas (vinculando turmas e estudantes).
* **Persistência de Dados:** Todos os dados são salvos e carregados de arquivos JSON, garantindo que as informações persistam entre as execuções do programa.

## 🚀 Como Executar o Projeto

Para rodar este projeto em sua máquina local, siga os passos abaixo:

1.  **Pré-requisitos:**
    * Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado em seu sistema.

2.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/biapeters/menu-atividade.git](https://github.com/biapeters/menu-atividade.git)
    ```

3.  **Navegue até o diretório do projeto:**
    ```bash
    cd menu-atividade
    ```

4.  **Execute o script principal:**
    ```bash
    python seu_script_principal.py # Substitua 'seu_script_principal.py' pelo nome do seu arquivo Python, se for diferente de 'main.py' ou similar. No seu caso, é o arquivo que contém as funções e o loop `while True:`.
    ```
    *(**Observação:** O nome do seu arquivo principal no repositório GitHub é `main.py`.)*
    ```bash
    python main.py
    ```

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **JSON:** Formato para persistência de dados em arquivos.

## 🧠 Aprendizados e Desafios

Este projeto foi uma excelente oportunidade para aplicar e reforçar conceitos fundamentais de programação, tais como:

* **Estruturas de Controle de Fluxo:** Utilização de laços de repetição (`while`, `for`) e condicionais (`if/elif/else`) para navegação e lógica do sistema.
* **Funções:** Organização do código em funções reutilizáveis para cada operação (incluir, listar, atualizar, excluir) e exibição de menus.
* **Estruturas de Dados:** Manipulação de listas de dicionários para armazenar e gerenciar os registros das entidades.
* **Manipulação de Arquivos:** Leitura e escrita de dados em arquivos JSON, garantindo a persistência das informações.
* **Tratamento de Exceções:** Implementação de blocos `try-except` para lidar com entradas inválidas do usuário (ex: `ValueError`).

O principal desafio foi garantir a robustez das operações CRUD e a consistência dos dados salvos e carregados, especialmente a validação de códigos únicos e a manipulação correta dos arquivos JSON.

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Made with ❤️ by Bianca Peters
