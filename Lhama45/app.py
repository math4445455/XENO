import os
import webbrowser
from flask import Flask, request, jsonify, render_template
from llm import gerar_resposta

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, "templates")
)

# Memória simples da conversa
historico = [
    {
        "role": "system",
        "content": "Você é a Lhama45, uma IA educada, clara e objetiva que responde em português."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    global historico

    dados = request.json
    pergunta = dados.get("texto", "").strip()

    if pergunta == "":
        return jsonify({"resposta": "Digite uma pergunta."})

    historico.append({"role": "user", "content": pergunta})

    resposta = gerar_resposta(historico)

    historico.append({"role": "assistant", "content": resposta})

    # Limita memória (economia de tokens)
    historico = historico[-10:]

    return jsonify({"resposta": resposta})

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=10000)