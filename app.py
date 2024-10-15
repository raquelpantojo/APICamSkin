import os
from flask import Flask, jsonify
from flask_cors import CORS
from pyngrok import ngrok

# Criação da aplicação Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route("/", methods=["GET"])  # Define o método HTTP para esta rota
def hello_world():
    # Retorna um JSON com as informações desejadas
    return jsonify({
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    })

if __name__ == '__main__':
    # Configuração do ngrok para expor o Flask
    NGROK_AUTH_TOKEN = "2nJVNuNAtMPRuZBFyVXTJXJbc9o_3Md6K1WyvQFzpfPwTurYJ"  # Insira o token do ngrok aqui
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)

    # Conectar ngrok à porta 5000
    public_url = ngrok.connect(5000)
    print(f" * Tunnel URL: {public_url}")

    # Iniciar o Flask
    app.run(port=5000)  # Especifica a porta para a aplicação Flask
