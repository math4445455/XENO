import os
import google.generativeai as genai

# O Render vai "injetar" a chave aqui automaticamente
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Coloque sua chave real aqui entre as aspas
genai.configure(api_key="AIzaSyBDJAmAgvq8arTBARoBuFRkeFeMxuyxMIQ")

# Configura o modelo e a personalidade da XENO
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Você é a XENO, uma IA educada, clara e objetiva que responde em português."
)

def gerar_resposta(historico):
    mensagens_anteriores = historico[:-1]
    mensagem_atual = historico[-1]["parts"][0]
    
    chat = model.start_chat(history=mensagens_anteriores)
    response = chat.send_message(mensagem_atual)
    
    return response.text
