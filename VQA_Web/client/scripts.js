let lastContext = "";

async function sendMessage() {
    const contextInput = document.getElementById("context-input");
    const questionInput = document.getElementById("question-input");

    const context = contextInput.value.trim() || lastContext;
    const question = questionInput.value;

    if (!context) {
        alert("Please provide context first!");
        return;
    }

    if (!question.trim()) {
        alert("Please provide a question!");
        return;
    }
    lastContext = context;

    const button = document.querySelector(".chat-input button");
    button.disabled = true;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

    const chatBox = document.getElementById("chat-box");
    if (contextInput.value.trim()) {
        const contextMessage = document.createElement("div");
        contextMessage.className = "message user";
        contextMessage.innerHTML = `
            <p><strong>Context:</strong> ${context}</p>
        `;
        chatBox.appendChild(contextMessage);
    }

    const questionMessage = document.createElement("div");
    questionMessage.className = "message user";
    questionMessage.innerHTML = `
        <p><strong>Question:</strong> ${question}</p>
    `;
    chatBox.appendChild(questionMessage);

    questionInput.value = "";
    contextInput.value = "";

    contextInput.placeholder = "Using previous context... (type to change)";

    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch("http://127.0.0.1:8000/vqa/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                context: context,
                question: question,
            }),
        });

        if (!response.ok) throw new Error("Network response was not ok");

        const data = await response.json();

        const aiMessage = document.createElement("div");
        aiMessage.className = "message ai";
        aiMessage.innerHTML = `
            <p>
                <strong>Answer:</strong> ${data.Answer}
                <span class="model-info">
                    <i class="fas fa-robot"></i> Model: ${data.Model}
                </span>
            </p>
        `;
        chatBox.appendChild(aiMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        console.error("Error:", error);
        const errorMessage = document.createElement("div");
        errorMessage.className = "message ai";
        errorMessage.innerHTML = `
            <p class="error"><strong>Error:</strong> Oops!! Có chuyện gì đó sai sai rồi.</p>
        `;
        chatBox.appendChild(errorMessage);
    } finally {
        button.disabled = false;
        button.innerHTML = '<i class="fas fa-paper-plane"></i> Send Message';
    }
}
