import click
from blockchain_connector import Blockchain


@click.group()
def cli():
    """Sistema de Recarga VE com Blockchain"""


@cli.command()
@click.argument('cliente_id')
@click.argument('posto_id')
def reservar(cliente_id, posto_id):
    """Faz uma reserva de posto"""
    bc = Blockchain()
    tx = bc.reservar_posto(cliente_id, posto_id)
    if tx:
        click.echo(f"✅ Reserva realizada: {tx}")
    else:
        click.echo("❌ Erro na reserva")


@cli.command()
@click.argument('cliente_id')
@click.argument('posto_id')
@click.argument('valor')
def pagar(cliente_id, posto_id, valor):
    """Realiza um pagamento"""
    bc = Blockchain()
    tx = bc.realizar_pagamento(cliente_id, posto_id, valor)
    if tx:
        click.echo(f"✅ Pagamento realizado: {tx}")
    else:
        click.echo("❌ Erro no pagamento")


@cli.command()
def historico():
    """Exibe o histórico de transações"""
    bc = Blockchain()
    transacoes = bc.get_historico()

    if not transacoes:
        click.echo("🟡 Nenhuma transação registrada")
        return

    click.echo("\n📜 Histórico de Transações\n" + "="*50)
    for i, tx in enumerate(transacoes, 1):
        click.echo(f"{i}. {tx.get('tipo')} | Cliente {tx.get('cliente_id')} | Posto {tx.get('posto_id')}")
        click.echo(f"   Data: {tx.get('data')}")
        click.echo(f"   Valor: {tx.get('valor', '---')}")
        click.echo(f"   Hash: {tx.get('hash')[:10]}...")
        click.echo("-"*50)


if __name__ == '__main__':
    cli()
