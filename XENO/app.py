import os
import webbrowser
from flask import Flask, request, jsonify, render_template
from llm import gerar_resposta

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, "templates")
)

# O histórico começará vazio. A instrução de sistema agora fica no llm.py
historico = []

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

    # Adiciona a pergunta no formato esperado pelo Gemini
    historico.append({"role": "user", "parts": [pergunta]})

    try:
        resposta = gerar_resposta(historico)
        
        # Adiciona a resposta da XENO (o Gemini usa a role "model")
        historico.append({"role": "model", "parts": [resposta]})
        
        # Mantém apenas as últimas 10 interações para não estourar o limite de tokens
        historico = historico[-10:]
        
        return jsonify({"resposta": resposta})
        
    except Exception as e:
        # Se der erro, remove a última pergunta para não quebrar o fluxo do histórico
        historico.pop()
        return jsonify({"resposta": f"Erro interno: {str(e)}"})

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=10000)