const socket = io(); // Conecta ao servidor

const usernameBox = document.getElementById('username-box');
const usernameInput = document.getElementById('username');
const enterChatButton = document.getElementById('enter-chat');

const chatBox = document.getElementById('chat');
const messages = document.getElementById('messages');
const input = document.getElementById('input');
const sendButton = document.getElementById('send');

let username = "";

// Solicitar o nome do usuário antes de entrar no chat
enterChatButton.addEventListener('click', () => {
    const enteredName = usernameInput.value.trim();
    if (enteredName) {
        username = enteredName;
        usernameBox.style.display = 'none';
        chatBox.style.display = 'block';
        socket.emit('set_username', username); // Envia o nome ao servidor
    } else {
        alert("Por favor, digite um nome.");
    }
});

// Recebe mensagens do servidor
socket.on('message', data => {
    const { user_id, message } = data;
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `
        <span class="username">${user_id}:</span> 
        <span class="message">${message}</span>
    `;
    messages.appendChild(messageElement);
    messages.scrollTop = messages.scrollHeight; // Scroll automático
});

// Envia mensagens ao servidor
sendButton.addEventListener('click', () => {
    const message = input.value.trim();
    if (message) {
        socket.send(message);
        input.value = ''; // Limpa o campo de entrada
    }
});

// Envia mensagem ao pressionar "Enter"
input.addEventListener('keypress', event => {
    if (event.key === 'Enter') {
        sendButton.click();
    }
});
