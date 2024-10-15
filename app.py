import os
from flask import Flask

app = Flask(__name__)

# Definindo uma rota simples
@app.route("/")
def hello_world():
    print("Endpoint / foi acessado")
    return "Hello, World!"

if __name__ == "__main__":
    # Obtém a porta da variável de ambiente (necessária no Render)
    
    # Executa a aplicação no host 0.0.0.0 para ser acessível externamente
    app.run(host="0.0.0.0")
