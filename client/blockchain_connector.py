import json
from fabric_sdk import Client, Network


class Blockchain:
    def __init__(self):
        self.network = Network('network.json')
        self.client = Client(self.network)

    def get_historico(self):
        try:
            response = self.client.query(
                channel='mychannel',
                chaincode='vechaincode',
                function='getAllTransactions'
            )
            return self._parse_response(response)
        except Exception as e:
            print(f"Erro ao consultar histórico: {str(e)}")
            return []

    def reservar_posto(self, cliente_id, posto_id):
        try:
            response = self.client.invoke(
                channel='mychannel',
                chaincode='vechaincode',
                function='reservarPosto',
                args={
                    "tipo": "reserva_posto",
                    "cliente_id": cliente_id,
                    "posto_id": posto_id
                }
            )
            return self._parse_response(response)
        except Exception as e:
            print(f"Erro ao reservar posto: {str(e)}")
            return None

    def realizar_pagamento(self, cliente_id, posto_id, valor):
        try:
            response = self.client.invoke(
                channel='mychannel',
                chaincode='vechaincode',
                function='realizarPagamento',
                args={
                    "tipo": "pagamento",
                    "cliente_id": cliente_id,
                    "posto_id": posto_id,
                    "valor": valor
                }
            )
            return self._parse_response(response)
        except Exception as e:
            print(f"Erro ao realizar pagamento: {str(e)}")
            return None

    def _parse_response(self, response):
        if not response.success:
            raise ValueError("Resposta inválida da blockchain")
        return json.loads(response.data)
