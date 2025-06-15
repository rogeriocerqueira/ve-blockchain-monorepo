#!/bin/bash

echo "🚀 Iniciando instalação do ambiente Blockchain Ethereum (Ganache + Truffle + Node.js)"

# 🔧 Atualizando pacotes
sudo apt update && sudo apt upgrade -y

# 🔧 Instalando dependências básicas
sudo apt install -y build-essential curl

# 🔥 Instalando Node.js LTS e npm via NodeSource
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

# ✅ Verificar Node e npm
node -v
npm -v

# 🔥 Configurando npm para instalação local (sem sudo)
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'

# ✔️ Adicionando no PATH
echo 'export PATH=$HOME/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# 🔥 Instalando Truffle global
npm install -g truffle

# 🔥 Instalando Ganache CLI global
npm install -g ganache

# ✔️ Verificar instalações
echo "✔️ Node.js versão: $(node -v)"
echo "✔️ npm versão: $(npm -v)"
echo "✔️ Truffle versão: $(truffle version)"
echo "✔️ Ganache versão: $(ganache --version)"

echo "✅ Ambiente Blockchain Ethereum instalado com sucesso!"
