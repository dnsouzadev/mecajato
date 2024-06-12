// temporary_message.js

// Seleciona todas as mensagens com a classe "js-temporary-message"
const temporaryMessages = document.querySelectorAll('.js-temporary-message');

// Remove a classe temporária após 2 segundos
temporaryMessages.forEach(function(message) {
    setTimeout(function() {
        message.classList.remove('js-temporary-message');
    }, 2000); // 2000 milissegundos = 2 segundos
});
