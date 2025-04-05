# DataProf

DataProf é uma aplicação web baseada em Django, criada para facilitar a gestão de dados escolares. O objetivo é proporcionar uma plataforma onde professores possam armazenar informações sobre seus alunos e organizar suas turmas de maneira simples e eficiente.

## Funcionalidades

- **Gestão de Alunos:** Cadastro e atualização de informações dos alunos.
- **Organização de Turmas:** Criação e gerenciamento de turmas e horários.
- **Autenticação Segura:** Controle de acesso para manter os dados protegidos.
- **Interface Responsiva:** Design moderno para uso em diferentes dispositivos.

## Instalação

### Requisitos

- Python 3.x
- Django 3.x ou superior
- Outras dependências listadas no arquivo `requirements.txt`

### Passos

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/Sistema_DataProf.git
   cd Sistema_DataProf

2. Crie e ative um ambiente virtual:

    No Linux/Mac:

python -m venv env
source env/bin/activate

No Windows:

    python -m venv env
    .\env\Scripts\activate

3. Instale as dependências:

pip install -r requirements.txt

Aplique as migrações do banco de dados:

python manage.py migrate

Inicie o servidor de desenvolvimento:

python manage.py runserver
