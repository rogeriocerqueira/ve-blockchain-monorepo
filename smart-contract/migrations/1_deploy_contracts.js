const RechargeContract = artifacts.require("RechargeContract");

module.exports = function (deployer) {
  deployer.deploy(RechargeContract);
};
