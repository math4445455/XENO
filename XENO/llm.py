import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("key.env")  # mantém compatibilidade local

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY não encontrada")

client = OpenAI(api_key=api_key)

def gerar_resposta(mensagem):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é a XENO, uma IA assistente amigável."},
            {"role": "user", "content": mensagem}
        ]
    )

    return response.choices[0].message.content