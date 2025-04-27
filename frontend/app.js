const outputField = document.getElementById('output');
let currentInput = '';

// Print instructions when page loads
printInstructions();

// Listen for key presses
document.addEventListener('keydown', function(event) {
    if (event.key === 'Backspace') {
        currentInput = currentInput.slice(0, -1);
    } else if (event.key.length === 1) {
        currentInput += event.key;
    } else if (event.key === 'Enter') {
        if (currentInput.trim() !== '') {
            printUserInput(currentInput);
            simulateResponse(currentInput);
            currentInput = '';
        }
        event.preventDefault(); // Prevent Enter key from doing weird things
    }

    refreshTerminal();
});

// Display current typing line with blinking cursor
function refreshTerminal() {
    const existingLines = outputField.dataset.history || '';
    outputField.innerHTML = existingLines +
        `<span style="color:#FFFFFF;">> ${currentInput}</span><span class="blinking-cursor">_</span>`;
    outputField.scrollTop = outputField.scrollHeight;
}

// Save user's input into terminal history
function printUserInput(input) {
    const existingLines = outputField.dataset.history || '';
    outputField.dataset.history = existingLines +
        `<span style="color:#FFFFFF;">> ${input}</span>\n`;
}

// Simulate a system response
function simulateResponse(userInput) {
    setTimeout(() => {
        const existingLines = outputField.dataset.history || '';
        outputField.dataset.history = existingLines +
            `<span style="color:#00FF00;">(system) You asked about: "${userInput}"</span>\n`;
        refreshTerminal();
    }, 500);
}

// Print startup instructions
function printInstructions() {
    const instructions = `
Welcome to RAG_ma_tax Terminal.

Instructions:
- Type your tax question below.
- Press ENTER to submit.
- Your input will appear in white.
- System responses will appear in green.
`;

    outputField.dataset.history = `<span style="color:#00FF00;">${instructions}</span>\n`;
    refreshTerminal();
}
