#!/bin/bash

echo "=============================="
echo "🚀 Iniciando Teste do Sistema Blockchain"
echo "=============================="

# Ativando ambiente Python
source ../client/venv/bin/activate

echo "🔗 Verificando histórico inicial..."
python3 ../client/main.py historico

echo "------------------------------"
echo "📍 Realizando reserva..."
python3 ../client/main.py reservar CLIENTE01 POSTO01

echo "------------------------------"
echo "💰 Realizando pagamento..."
python3 ../client/main.py pagar CLIENTE01 POSTO01 0.5

echo "------------------------------"
echo "🔋 Iniciando recarga..."
python3 ../client/main.py iniciar CLIENTE01 POSTO01

echo "------------------------------"
echo "🏁 Finalizando recarga..."
python3 ../client/main.py finalizar CLIENTE01 POSTO01

echo "------------------------------"
echo "📜 Consultando histórico final..."
python3 ../client/main.py historico

echo "=============================="
echo "✅ Teste concluído com sucesso!"
echo "=============================="
