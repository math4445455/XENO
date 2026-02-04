import os
from flask import Flask, request, jsonify, render_template
from llm import gerar_resposta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Mensagem inválida"}), 400

    try:
        resposta = gerar_resposta(data["message"])
        return jsonify({"reply": resposta})
    except Exception as e:
        print("Erro:", e)
        return jsonify({"reply": "Erro interno no servidor."}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)