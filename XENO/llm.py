import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resposta(mensagens):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=mensagens,
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content
