import json
import hashlib
from datetime import datetime


class Response:
    def __init__(self, success: bool, data: str):
        self.success = success
        self.data = data


class Client:
    def __init__(self, network):
        self.network = network
        self.ledger = []  # 🔗 Simula o ledger blockchain
        print("🟢 Cliente blockchain inicializado com a rede simulada.")

    def query(self, channel: str, chaincode: str, function: str):
        """
        Consulta o ledger (blockchain simulada).
        """
        print(f"📡 Query -> Canal: {channel}, Chaincode: {chaincode}, Função: {function}")

        data_json = json.dumps(self.ledger)
        return Response(success=True, data=data_json)

    def invoke(self, channel: str, chaincode: str, function: str, args: dict):
        """
        Escreve uma nova transação no ledger.
        """
        print(f"🚀 Invoke -> Canal: {channel}, Chaincode: {chaincode}, Função: {function}")

        # Gera um hash simples para simular a integridade da transação
        hash_input = json.dumps(args) + str(datetime.now())
        tx_hash = hashlib.sha256(hash_input.encode()).hexdigest()

        transacao = {
            "tipo": args.get("tipo"),
            "cliente_id": args.get("cliente_id"),
            "posto_id": args.get("posto_id"),
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "valor": args.get("valor", None),
            "hash": tx_hash
        }

        self.ledger.append(transacao)

        return Response(success=True, data=json.dumps(transacao))
