async function sendMessage() {
    const context = document.getElementById("context-input").value;
    const question = document.getElementById("question-input").value;

    if (context.trim() === "" || question.trim() === "") {
        alert("Please provide both context and question.");
        return;
    }

    const chatBox = document.getElementById("chat-box");
    const contextMessage = document.createElement("div");
    contextMessage.className = "message user";
    contextMessage.innerHTML = `
        <p><strong>Context:</strong> ${context}</p>
    `;
    chatBox.appendChild(contextMessage);

    const questionMessage = document.createElement("div");
    questionMessage.className = "message user";
    questionMessage.innerHTML = `
        <p><strong>Question:</strong> ${question}</p>
    `;
    chatBox.appendChild(questionMessage);

    document.getElementById("context-input").value = "";
    document.getElementById("question-input").value = "";

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
            <p><strong>Answer:</strong> ${data.Answer}</p>
        `;
        chatBox.appendChild(aiMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        console.error("Error:", error);
    }
}
