import os
from flask import Flask, send_from_directory
from flask_socketio import SocketIO, send, emit

# Configuração do servidor
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Rota para servir a interface do cliente
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')  # Corrigido para buscar na pasta static

# Gerenciar mensagens enviadas pelos clientes
@socketio.on('message')
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")
    # Envia a mensagem para todos os clientes conectados
    send(msg, broadcast=True)

# Inicialização do servidor
if __name__ == '__main__':
    host = '127.0.0.1'
    port = int(os.getenv("PORT", 5000))  # Lê a variável PORT ou usa 5000 como padrão
    print(f"Servidor rodando em http://{host}:{port}")
    socketio.run(app, host=host, port=port)
