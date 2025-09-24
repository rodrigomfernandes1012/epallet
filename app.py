from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtém os dados recebidos no corpo da requisição
    data = request.get_json()

    # Converte os dados para uma string (se necessário)
    data_str = str(data)

    # Grava os dados em um arquivo txt
    with open('dados_webhook.txt', 'a') as f:
        f.write(data_str + '\n')

    # Retorna uma resposta visual no navegador
    return f"<h1>Dados recebidos:</h1><pre>{data_str}</pre>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
