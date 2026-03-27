@app.route("/perguntar", methods=["POST"])
def perguntar():
    global historico
    dados = request.json
    pergunta = dados.get("texto", "").strip()

    if not pergunta:
        return jsonify({"resposta": "Digite uma pergunta."})

    historico.append({"role": "user", "content": pergunta})
    
    # Chama a função atualizada do llm.py
    resposta = gerar_resposta(historico)

    # O Gemini usa 'model', mas para manter seu histórico interno:
    historico.append({"role": "assistant", "content": resposta})
    historico = historico[-10:]

    return jsonify({"resposta": resposta})
