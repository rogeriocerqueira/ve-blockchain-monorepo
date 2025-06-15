// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RechargeContract {

    enum Tipo { Reserva, Pagamento, IniciarRecarga, FinalizarRecarga }
    enum Status { Ativo, Concluido }

    struct Transacao {
        uint id;
        Tipo tipo;
        string clienteId;
        string postoId;
        uint valor;
        uint timestamp;
        Status status;
    }

    uint public contador;
    Transacao[] public transacoes;

    // 🔗 Controle de status dos postos
    mapping(string => bool) public postoReservado;
    mapping(string => bool) public postoEmRecarga;

    event NovaTransacao(
        uint id,
        Tipo tipo,
        string clienteId,
        string postoId,
        uint valor,
        uint timestamp,
        Status status
    );

    constructor() {
        contador = 0;
    }

    // 🔵 Reserva de posto
    function reservarPosto(string memory clienteId, string memory postoId) public {
        require(!postoReservado[postoId], "Posto ja reservado.");
        postoReservado[postoId] = true;
        _criarTransacao(Tipo.Reserva, clienteId, postoId, 0);
    }

    // 💰 Pagamento
    function realizarPagamento(string memory clienteId, string memory postoId) public payable {
        require(msg.value > 0, "Pagamento deve ser maior que zero.");
        require(postoReservado[postoId], "Posto nao reservado.");
        _criarTransacao(Tipo.Pagamento, clienteId, postoId, msg.value);
    }

    // 🔋 Iniciar Recarga
    function iniciarRecarga(string memory clienteId, string memory postoId) public {
        require(postoReservado[postoId], "Posto nao reservado.");
        require(!postoEmRecarga[postoId], "Posto ja em recarga.");
        postoEmRecarga[postoId] = true;
        _criarTransacao(Tipo.IniciarRecarga, clienteId, postoId, 0);
    }

    // 🏁 Finalizar Recarga
    function finalizarRecarga(string memory clienteId, string memory postoId) public {
        require(postoEmRecarga[postoId], "Posto nao esta em recarga.");
        postoReservado[postoId] = false;
        postoEmRecarga[postoId] = false;
        _criarTransacao(Tipo.FinalizarRecarga, clienteId, postoId, 0);
    }

    // 📜 Consulta histórico completo
    function consultarHistorico() public view returns (Transacao[] memory) {
        return transacoes;
    }

    // 🔧 Função interna de criação de transações
    function _criarTransacao(
        Tipo tipo,
        string memory clienteId,
        string memory postoId,
        uint valor
    ) internal {
        contador++;

        Transacao memory t = Transacao({
            id: contador,
            tipo: tipo,
            clienteId: clienteId,
            postoId: postoId,
            valor: valor,
            timestamp: block.timestamp,
            status: Status.Ativo
        });

        transacoes.push(t);

        emit NovaTransacao(
            t.id,
            t.tipo,
            t.clienteId,
            t.postoId,
            t.valor,
            t.timestamp,
            t.status
        );
    }
}
