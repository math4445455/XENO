from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

# Cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    data = request.get_json()
    pergunta = data.get("texto", "")

    if pergunta.strip() == "":
        return jsonify({"resposta": "Digite uma pergunta."})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é a Lhama45, uma IA inteligente e amigável."},
                {"role": "user", "content": pergunta}
            ]
        )

        resposta = response.choices[0].message.content
        return jsonify({"resposta": resposta})

    except Exception as e:
        return jsonify({"resposta": f"Erro na IA: {str(e)}"})
