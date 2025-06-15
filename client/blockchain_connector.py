from web3 import Web3
import json
from dotenv import load_dotenv



class BlockchainConnector:
    def __init__(self):
        ganache_url = "http://ganache:7545"
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))
        assert self.web3.is_connected(), "❌ Erro de conexão com Ganache!"

        with open('abi.json') as f:
            abi = json.load(f)

        with open('contract_address.txt') as f:
            contract_address = f.read().strip()

        self.contract = self.web3.eth.contract(
            address=contract_address,
            abi=abi
        )

        self.account = self.web3.eth.accounts[0]  # Conta padrão

    def reservar_posto(self, cliente_id, posto_id):
        tx_hash = self.contract.functions.reservarPosto(
            cliente_id, posto_id
        ).transact({'from': self.account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"✅ Reserva realizada - Hash: {tx_hash.hex()}")

    def realizar_pagamento(self, cliente_id, posto_id, valor_eth):
        valor_wei = self.web3.to_wei(valor_eth, 'ether')
        tx_hash = self.contract.functions.realizarPagamento(
            cliente_id, posto_id
        ).transact({'from': self.account, 'value': valor_wei})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"✅ Pagamento realizado - Hash: {tx_hash.hex()}")

    def iniciar_recarga(self, cliente_id, posto_id):
        tx_hash = self.contract.functions.iniciarRecarga(
            cliente_id, posto_id
        ).transact({'from': self.account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"🔋 Recarga iniciada - Hash: {tx_hash.hex()}")

    def finalizar_recarga(self, cliente_id, posto_id):
        tx_hash = self.contract.functions.finalizarRecarga(
            cliente_id, posto_id
        ).transact({'from': self.account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"🏁 Recarga finalizada - Hash: {tx_hash.hex()}")

    def consultar_historico(self):
        historico = self.contract.functions.consultarHistorico().call()
        print("📜 Histórico de Transações:")
        for tx in historico:
            print(f"ID: {tx[0]}, Tipo: {tx[1]}, Cliente: {tx[2]}, Posto: {tx[3]}, Valor: {self.web3.from_wei(tx[4], 'ether')} ETH, Timestamp: {tx[5]}, Status: {tx[6]}")
