from server.blockchain_connector import BlockchainConnector

blockchain = BlockchainConnector()

def cadastrar_cliente(data):
    cliente_id = data.get('cliente')
    try:
        receipt = blockchain.execute_transaction('cadastrarCliente', cliente_id)
        return {"status": "Cliente cadastrado", "tx": receipt.transactionHash.hex()}
    except Exception as e:
        return {"error": str(e)}
