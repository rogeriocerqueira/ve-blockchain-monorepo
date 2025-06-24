from server.blockchain_connector import BlockchainConnector

blockchain = BlockchainConnector()

def fazer_reserva(data):
    cliente = data.get('cliente')
    posto = data.get('posto')
    try:
        receipt = blockchain.execute_transaction('reservarPosto', cliente, posto)
        return {"status": "Reserva realizada", "tx": receipt.transactionHash.hex()}
    except Exception as e:
        return {"error": str(e)}
