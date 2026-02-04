const chatBox = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.className = sender;
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function enviarMensagem() {
    const texto = input.value.trim();
    if (!texto) return;

    addMessage(texto, "user");
    input.value = "";

    const typing = document.createElement("div");
    typing.className = "bot";
    typing.innerText = "XENO está digitando...";
    chatBox.appendChild(typing);

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: texto })
        });

        const data = await response.json();
        typing.remove();
        addMessage(data.reply, "bot");

    } catch (e) {
        typing.remove();
        addMessage("Erro ao conectar ao servidor.", "bot");
    }
}

sendBtn.onclick = enviarMensagem;
input.addEventListener("keydown", e => {
    if (e.key === "Enter") enviarMensagem();
});