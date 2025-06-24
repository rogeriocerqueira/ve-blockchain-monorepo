from flask import Flask, jsonify, request
from services import reservation_service, status_service, client_service, history_service

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API do Sistema de Recarga funcionando."})

# Cadastro de Cliente
@app.route('/cliente', methods=['POST'])
def cadastrar_cliente():
    data = request.json
    result = client_service.cadastrar_cliente(data)
    return jsonify(result)

# Fazer Reserva
@app.route('/reserva', methods=['POST'])
def fazer_reserva():
    data = request.json
    result = reservation_service.fazer_reserva(data)
    return jsonify(result)

# Status dos Postos
@app.route('/status', methods=['GET'])
def status():
    return jsonify(status_service.listar_status())

# Histórico
@app.route('/historico', methods=['GET'])
def historico():
    return jsonify(history_service.consultar_historico())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
