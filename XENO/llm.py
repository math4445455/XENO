import os
import google.generativeai as genai
from dotenv import load_dotenv

# carrega key.env
load_dotenv("key.env")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY não definida no ambiente")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash"
)

def gerar_resposta(mensagens):
    """
    mensagens = [
        {"role": "user", "content": "Olá"},
        {"role": "assistant", "content": "Oi!"},
        {"role": "user", "content": "Explique algo"}
    ]
    """

    prompt = ""
    for msg in mensagens:
        if msg["role"] == "system":
            prompt += f"Instruções: {msg['content']}\n\n"
        elif msg["role"] == "user":
            prompt += f"Usuário: {msg['content']}\n"
        elif msg["role"] == "assistant":
            prompt += f"Assistente: {msg['content']}\n"

    response = model.generate_content(prompt)

    return response.text