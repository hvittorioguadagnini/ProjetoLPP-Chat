const socket = io(); // Conecta ao servidor

const messages = document.getElementById('messages');
const input = document.getElementById('input');
const sendButton = document.getElementById('send');

// Recebe mensagens do servidor
socket.on('message', msg => {
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `
        <span class="username">Usuário:</span> 
        <span class="message">${msg}</span>
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
