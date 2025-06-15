#!/bin/bash

echo "🚀 Inicializando setup da blockchain..."

cd smart-contract

echo "📦 Instalando dependências..."
npm install

echo "🛠️ Compilando contratos..."
truffle compile

echo "🚀 Realizando deploy dos contratos no Ganache..."
truffle migrate --reset

echo "📄 Gerando abi.json..."
cat build/contracts/PostoRecarga.json | jq '.abi' > ../client/abi.json

echo "📜 Salvando contract_address.txt..."
ADDRESS=$(cat build/contracts/PostoRecarga.json | jq -r '.networks | to_entries[0].value.address')
echo $ADDRESS > ../client/contract_address.txt

echo "✅ Setup completo! ABI e endereço do contrato salvos em /client"
