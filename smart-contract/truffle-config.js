module.exports = {
  compilers: {
    solc: {
      version: "0.8.0",
      settings: {
        optimizer: {
          enabled: true,
          runs: 200
        }
      }
    }
  },
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*",
      gas: 6600000, // 🔥 Abaixo do limite do bloco
      gasPrice: 20000000000 // 20 Gwei
    }
  }
};
