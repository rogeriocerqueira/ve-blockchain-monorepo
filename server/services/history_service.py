from server.blockchain_connector import BlockchainConnector

blockchain = BlockchainConnector()

def consultar_historico():
    try:
        historico = blockchain.call_function('consultarHistorico')
        lista = []
        for item in historico:
            lista.append({
                "id": item[0],
                "tipo": item[1],
                "cliente": item[2],
                "posto": item[3],
                "valor": item[4],
                "timestamp": item[5],
                "status": item[6]
            })
        return lista
    except Exception as e:
        return {"error": str(e)}
