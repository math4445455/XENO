const chat = document.getElementById("chat");
const input = document.getElementById("input");
const typing = document.getElementById("typing");
const settings = document.getElementById("settings");

let lang = localStorage.getItem("lang") || "pt";

document.body.classList.toggle("light", localStorage.getItem("theme") === "light");

document.getElementById("settingsBtn").onclick = () => {
  settings.classList.toggle("hidden");
};

function closeSettings() {
  settings.classList.add("hidden");
}

function toggleTheme() {
  document.body.classList.toggle("light");
  localStorage.setItem(
    "theme",
    document.body.classList.contains("light") ? "light" : "dark"
  );
}

function clearChat() {
  chat.innerHTML = "";
}

function changeLang(value) {
  lang = value;
  localStorage.setItem("lang", value);
}

function addMessage(text, cls) {
  const div = document.createElement("div");
  div.className = `message ${cls}`;
  div.innerText = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function sendMessage() {
  const msg = input.value.trim();
  if (!msg) return;

  addMessage(msg, "user");
  input.value = "";

  typing.classList.remove("hidden");

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg, lang })
    });

    const data = await res.json();
    addMessage(data.reply || "Erro ao responder.", "bot");

  } catch {
    addMessage("Erro de conexão.", "bot");
  }

  typing.classList.add("hidden");
}