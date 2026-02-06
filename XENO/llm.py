import os
import google.generativeai as genai
from dotenv import load_dotenv

# Tenta carregar o arquivo de configuração. 
# Se estiver no Render, você deve configurar a chave nas 'Environment Variables' do painel.
load_dotenv("key.env")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("ERRO: GEMINI_API_KEY não encontrada. Verifique seu arquivo key.env ou as variáveis de ambiente.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash"
)

def gerar_resposta(mensagens):
    """
    Formata o histórico e envia para o Gemini.
    """
    prompt = ""
    for msg in mensagens:
        if msg["role"] == "system":
            prompt += f"Instruções: {msg['content']}\n\n"
        elif msg["role"] == "user":
            prompt += f"Usuário: {msg['content']}\n"
        elif msg["role"] == "assistant":
            prompt += f"Assistente: {msg['content']}\n"

    try:
        response = model.generate_content(prompt)
        
        # Verifica se a resposta contém texto (evita erro se for bloqueada por segurança)
        if response.candidates and response.text:
            return response.text
        else:
            return "O Gemini não conseguiu gerar uma resposta para esta pergunta."
            
    except Exception as e:
        print(f"Erro detalhado na API: {e}")
        return "Erro ao processar sua pergunta na IA."