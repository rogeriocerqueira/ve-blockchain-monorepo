import click
from blockchain_connector import BlockchainConnector

@click.group()
def cli():
    pass

@cli.command()
@click.argument('cliente_id')
@click.argument('posto_id')
def reservar(cliente_id, posto_id):
    bc = BlockchainConnector()
    bc.reservar_posto(cliente_id, posto_id)

@cli.command()
@click.argument('cliente_id')
@click.argument('posto_id')
@click.argument('valor')
def pagar(cliente_id, posto_id, valor):
    bc = BlockchainConnector()
    bc.realizar_pagamento(cliente_id, posto_id, float(valor))

@cli.command()
@click.argument('cliente_id')
@click.argument('posto_id')
def iniciar(cliente_id, posto_id):
    bc = BlockchainConnector()
    bc.iniciar_recarga(cliente_id, posto_id)

@cli.command()
@click.argument('cliente_id')
@click.argument('posto_id')
def finalizar(cliente_id, posto_id):
    bc = BlockchainConnector()
    bc.finalizar_recarga(cliente_id, posto_id)

@cli.command()
def historico():
    bc = BlockchainConnector()
    bc.consultar_historico()

if __name__ == '__main__':
    cli()
