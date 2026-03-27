import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# O Render lerá GEMINI_API_KEY do painel Environment
chave = os.getenv("GEMINI_API_KEY")
if not chave:
    print("ERRO: GEMINI_API_KEY não encontrada!")

genai.configure(api_key=chave)

# Configuração do modelo Gemini
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Você é a XENO, uma IA educada, clara e objetiva que responde em português."
)

def gerar_resposta(mensagens):
    # O app.py envia o histórico completo. Pegamos a última pergunta:
    pergunta_usuario = mensagens[-1]["content"]
    
    try:
        response = model.generate_content(pergunta_usuario)
        return response.text
    except Exception as e:
        return f"Erro na API do Gemini: {str(e)}"
