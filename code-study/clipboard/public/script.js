const textarea = document.getElementById('clipboard');
const charCount = document.getElementById('charCount');
const storageKey = 'sharedClipboard';

// Function to update character count
function updateCharCount() {
    const maxLength = 500;
    const currentLength = textarea.value.length;
    const remaining = maxLength - currentLength;

    charCount.textContent = `Characters left: ${remaining}`;
}

// Function to handle changes in the textarea
function handleTextareaChange() {
    updateCharCount();
    // Send update to server (via AJAX or WebSocket)
    saveToServer(textarea.value);
}

// Function to save content to server
function saveToServer(content) {
    // Example using fetch API
    fetch('/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to save clipboard content.');
        }
    })
    .catch(error => {
        console.error('Error saving clipboard content:', error);
    });
}

// Load saved content if available (on page reload)
window.onload = function() {
    // Fetch initial content from server
    fetch('/load')
    .then(response => response.json())
    .then(data => {
        textarea.value = data.content;
        updateCharCount(); // Update character count on load
    })
    .catch(error => {
        console.error('Error loading clipboard content:', error);
    });
};

// Listen for changes in the textarea
textarea.addEventListener('input', handleTextareaChange);
