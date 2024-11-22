// Get references to the DOM elements
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const languageSelect = document.getElementById('language-select');

// Hardcoded username for demonstration (replace with actual logic for fetching username if needed)
const username = 'madhu05';  // Replace with actual logic for fetching username

// Event listener for the Send button
sendBtn.addEventListener('click', function() {
    sendMessage();
});

// Event listener for pressing 'Enter' key in the input box
userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Function to show a loading indicator
function showLoadingMessage() {
    const messageElement = document.createElement('div');
    messageElement.className = 'bot loading';
    messageElement.textContent = 'Bot is thinking...';
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;  // Ensure the chat scrolls to the bottom
}

// Function to remove the loading indicator
function removeLoadingMessage() {
    const loadingElement = document.querySelector('.bot.loading');
    if (loadingElement) {
        loadingElement.remove();
    }
}

// Function to send the user message to the backend
function sendMessage() {
    const message = userInput.value.trim();
    const selectedLanguage = languageSelect.value;

    // Limit the length of user input
    if (message.length > 300) {
        alert("Please keep your message under 300 characters.");
        return;
    }

    if (message === '') return;

    // Display user's message in the chat box
    addChatMessage('User', message);
    showLoadingMessage();  // Show loading indicator

    // Prepare data to send to the backend
    const data = {
        message: message,
        user_id: username, // Send username instead of user_id
        language: selectedLanguage  // Send the selected language
    };

    // Send the message to the backend via a POST request
    fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        removeLoadingMessage();  // Remove loading indicator
        const botMessage = data.response || 'No response from the server.';
        
        // Check if the bot message contains guidance (i.e., tracking "yes" or "no")
        if (botMessage.toLowerCase().includes('would you like me to guide you')) {
            addChatMessage('Bot', botMessage); // Add bot question about guidance
        } else {
            addChatMessage('Bot', botMessage); // Normal bot response
        }
    })
    .catch(error => {
        console.error('Error:', error);
        removeLoadingMessage();  // Remove loading indicator
        addChatMessage('Bot', 'There was an error processing your request. Please try again.');
    });

    // Clear the input field after sending the message
    userInput.value = '';
}

// Function to add a chat message to the chat box
function addChatMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.className = sender.toLowerCase(); // 'user' or 'bot'
    messageElement.textContent = `${sender}: ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll to the latest message
}

// Function to add initial greeting message (called when chat is first loaded)
function addGreetingMessage() {
    const greetingElement = document.createElement('div');
    greetingElement.className = 'bot';
    greetingElement.textContent = `Hello ${username}! I’m here to support you during your pregnancy. How can I help you today?`;
    chatBox.appendChild(greetingElement);
    chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll to the latest message
}

// Add the greeting message when the page loads
window.onload = function() {
    addGreetingMessage();
};

// Function to detect language change and show a message
languageSelect.addEventListener('change', function() {
    const selectedLanguage = languageSelect.options[languageSelect.selectedIndex].text;
    addChatMessage('Bot', `Language changed to ${selectedLanguage}.`);
});
