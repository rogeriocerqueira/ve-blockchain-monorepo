from server.blockchain_connector import BlockchainConnector

blockchain = BlockchainConnector()

def listar_status():
    try:
        status = blockchain.call_function('consultarStatusPostos')
        return {"status_postos": status}
    except Exception as e:
        return {"error": str(e)}
