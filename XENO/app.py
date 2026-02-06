import os
from flask import Flask, request, jsonify, render_template
from llm import gerar_resposta

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, "templates"),
    static_folder=os.path.join(base_dir, "static")
)

historico = [
    {
        "role": "system",
        "content": "Você é a XENO, uma IA educada, clara e objetiva que responde em português."
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    global historico

    try:
        dados = request.get_json(force=True)
        pergunta = dados.get("texto", "").strip()

        if not pergunta:
            return jsonify({"resposta": "Digite uma pergunta."})

        historico.append({"role": "user", "content": pergunta})

        resposta = gerar_resposta(historico)

        historico.append({"role": "assistant", "content": resposta})
        historico = historico[-10:]

        return jsonify({"resposta": resposta})

    except Exception as e:
        print("ERRO:", e)
        return jsonify({"resposta": "Erro interno no servidor."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))