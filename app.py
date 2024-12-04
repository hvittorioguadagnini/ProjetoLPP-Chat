import os
from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, emit, send

# Configuração do servidor
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Armazena os usuários conectados
connected_users = {}

# Rota para servir a interface do cliente
@app.route('/')
def index():
    try:
        return send_from_directory('static', 'index.html')
    except Exception as e:
        print(f"Erro ao servir o arquivo: {e}")
        return "Erro ao carregar a interface.", 500

# Recebe o nome do usuário ao conectar
@socketio.on('set_username')
def handle_set_username(username):
    try:
        connected_users[request.sid] = username
        print(f"Usuário conectado: {username} ({request.sid})")
    except Exception as e:
        print(f"Erro ao setar nome de usuário: {e}")
        emit('error', 'Erro ao configurar o nome de usuário.')

# Evento de desconexão
@socketio.on('disconnect')
def handle_disconnect():
    try:
        username = connected_users.pop(request.sid, None)
        if username:
            print(f"{username} desconectado.")
    except Exception as e:
        print(f"Erro durante desconexão: {e}")

# Gerenciar mensagens enviadas pelos clientes
@socketio.on('message')
def handle_message(msg):
    try:
        username = connected_users.get(request.sid, "Usuário Anônimo")
        print(f"{username} enviou: {msg}")
        # Envia a mensagem para todos os clientes conectados
        emit('message', {'user_id': username, 'message': msg}, broadcast=True)
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        emit('error', 'Erro ao processar sua mensagem.')

# Inicialização do servidor
if __name__ == '__main__':
    try:
        # host('127.0.0.1' ou 'localhost') para ambiente de teste:
        # host = 'localhost'

        # host para deploy:
        host = '0.0.0.0'

        port = int(os.getenv("PORT", 5000))  # Lê a variável PORT ou usa 5000 como padrão

        print(f"Servidor rodando em http://{host}:{port}")

        socketio.run(app, host=host, port=port)
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")
