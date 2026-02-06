import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY não definida no ambiente")

client = OpenAI(api_key=API_KEY)

def gerar_resposta(mensagens):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=mensagens,
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content