import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Tenta pegar do .env ou das variáveis de ambiente do Render
chave = os.getenv("GEMINI_API_KEY")

if not chave:
    raise ValueError("A chave GEMINI_API_KEY não foi encontrada nas variáveis de ambiente!")

genai.configure(api_key=chave)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Você é a XENO, uma IA educada, clara e objetiva que responde em português."
)

def gerar_resposta(mensagens):
    # O Gemini precisa de um formato específico. Vamos converter o que vem do app.py
    # O app.py envia uma lista de dicts. Vamos pegar apenas o conteúdo da última.
    pergunta_usuario = mensagens[-1]["content"]
    
    response = model.generate_content(pergunta_usuario)
    return response.text
