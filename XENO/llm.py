import os
import google.generativeai as genai

# O Render vai ler a chave que você colocou no painel Environment
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Você é a XENO, uma IA educada, clara e objetiva que responde em português."
)

def gerar_resposta(historico):
    # Converte o histórico do formato OpenAI para o formato Gemini
    gemini_history = []
    for msg in historico:
        role = "user" if msg["role"] == "user" else "model"
        # Ignora mensagens de 'system' que o Gemini já recebeu na config do model
        if msg["role"] != "system":
            gemini_history.append({"role": role, "parts": [msg["content"]]})
    
    # Pega a última mensagem enviada
    ultima_msg = gemini_history.pop()["parts"][0]
    
    chat = model.start_chat(history=gemini_history)
    response = chat.send_message(ultima_msg)
    
    return response.text
