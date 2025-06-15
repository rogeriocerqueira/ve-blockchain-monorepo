module.exports = {
  networks: {
    development: {
      host: "ganache", // nome do serviço no docker-compose
      port: 7545,
      network_id: "*",
      networkCheckTimeout: 100000
    }
  },
  compilers: {
    solc: {
      version: "0.8.30"
    }
  }
};
