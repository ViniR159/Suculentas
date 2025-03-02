
# Suculentas 🌵

Um sistema simples e eficiente para gerenciar produtos relacionados a suculentas. Este projeto foi desenvolvido utilizando **Python Flask** para a estrutura backend e um banco de dados **SQL** para armazenar os produtos.

## 📋 Funcionalidades

- **Cadastro de Produtos**: Adicione novas suculentas ao catálogo com informações como nome, descrição, preço e imagem.
- **Listagem de Produtos**: Visualize todos os produtos cadastrados no banco de dados.
- **Atualização de Produtos**: Edite informações de produtos existentes.
- **Exclusão de Produtos**: Remova produtos do catálogo facilmente.
- **Integração com Banco de Dados**: Os dados dos produtos são armazenados de forma segura e eficiente em um banco de dados SQL.

## 🛠️ Tecnologias Utilizadas

- **Python Flask**: Framework para desenvolvimento web.
- **SQL**: Banco de dados para armazenamento de informações dos produtos.
- **HTML/CSS**: Interface básica para interação com o sistema.
- **Jinja2**: Template engine para renderizar páginas dinâmicas.

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/ViniR159/Suculentas.git
   cd Suculentas
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure o banco de dados:
   - Certifique-se de que o arquivo de configuração do banco de dados (`config.py`) está configurado corretamente.
   - Execute as migrações (se necessário) para criar as tabelas.

4. Inicie o servidor:

   ```bash
   flask run
   ```

5. Acesse o sistema em [http://localhost:5000](http://localhost:5000).

## 🚀 Como Usar

1. Acesse a página inicial do sistema.
2. Adicione novos produtos utilizando o formulário de cadastro.
3. Visualize, edite ou exclua produtos já cadastrados.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias no sistema.
