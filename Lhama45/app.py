from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.json
    texto = dados.get("texto", "")
    modo = dados.get("modo", "texto")

    if modo == "imagem":
        imagens = buscar_imagens(texto)
        return jsonify({"imagens": imagens})

    return jsonify({
        "resposta": f"Você perguntou: {texto}\n\n(Essa resposta pode ser ligada à API OpenAI)"
    })

def buscar_imagens(consulta):
    base = "https://source.unsplash.com/featured/?"
    return [
        base + consulta,
        base + consulta + ",1",
        base + consulta + ",2"
    ]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)