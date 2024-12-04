# ProjetoLPP-Chat

Este projeto é uma aplicação de **chat em tempo real** desenvolvida utilizando **Flask** e **Socket.IO**. O objetivo é proporcionar uma plataforma para comunicação instantânea entre usuários, com funcionalidades de gerenciamento de conexões e mensagens. O sistema é projetado para ser escalável, modular e eficiente, utilizando conceitos de **programação orientada a objetos**, **reativa**, **imperativa** e **funcional**.

## Funcionalidades

- **Conexão de usuários**: O sistema permite que os usuários se conectem e definam seus nomes.
- **Envio de mensagens em tempo real**: Mensagens são enviadas e recebidas instantaneamente, permitindo a comunicação contínua.
- **Desconexão de usuários**: Quando um usuário se desconecta, o sistema registra a saída e limpa os dados correspondentes.
- **Erros tratados**: O sistema lida com erros de maneira eficiente, garantindo uma experiência robusta para o usuário.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python, usado para a criação do servidor.
- **Socket.IO**: Biblioteca para comunicação em tempo real via WebSockets.
- **Python**: Linguagem de programação usada no desenvolvimento da aplicação.
- **Jinja2**: Template engine utilizada pelo Flask para renderizar páginas HTML.

Aqui está o texto completo do README com a formatação adequada para o GitHub, utilizando os `#` para os títulos e subseções:

```markdown


## Como Rodar o Projeto

### Clonar o repositório:

```bash
git clone https://github.com/seu-usuario/ProjetoLPP-Chat.git
cd ProjetoLPP-Chat
```

### Instalar as dependências:

Utilize o `pip` para instalar as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Rodar a aplicação:

Execute o servidor:

```bash
python app.py
```

O servidor estará disponível em `http://localhost:5000` ou `http://127.0.0.1:5000` para ambiente local e em `0.0.0.0` para produção.

## Como Funciona

- O servidor é iniciado com **Flask** e **Socket.IO**, onde a comunicação em tempo real é gerenciada por **WebSockets**.
- O cliente se conecta ao servidor e envia o nome de usuário para o sistema.
- O servidor emite mensagens para todos os clientes conectados, permitindo que as mensagens sejam compartilhadas em tempo real.
- O sistema também garante que, ao desconectar um usuário, o nome associado seja removido.

