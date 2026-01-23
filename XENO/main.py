import os
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from openai import OpenAI

if os.path.exists("key.env"):
    load_dotenv("key.env")
else:
    load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY não encontrada. Verifique o arquivo key.env ou as variáveis do Render.")

client = OpenAI(api_key=API_KEY)

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    mensagem = data.get("message", "").strip()

    if not mensagem:
        return jsonify({"error": "Mensagem vazia"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é XENO, uma IA assistente inteligente, clara e amigável."},
                {"role": "user", "content": mensagem}
            ]
        )

        resposta = response.choices[0].message.content
        return jsonify({"reply": resposta})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)