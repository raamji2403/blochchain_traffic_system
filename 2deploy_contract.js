const TrafficLight = artifacts.require("TrafficLight");

module.exports = function(deployer) {
    deployer.deploy(TrafficLight);
};
