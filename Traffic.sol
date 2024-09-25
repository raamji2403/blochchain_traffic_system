pragma solidity 0.8.19;

contract TrafficLight {
    struct Pole {
        uint id;
        string signal;
        uint lastUpdated;
    }
    mapping(uint => Pole) public poles;
    uint public poleCount = 0;
    event PoleAdded(uint id, string signal, uint lastUpdated);
    event SignalChanged(uint id, string newSignal, uint lastUpdated);
    function addPole() public {
        poleCount++;
        poles[poleCount] = Pole(poleCount, "Red", block.timestamp);
        emit PoleAdded(poleCount, "Red", block.timestamp);
    }
    function changeSignal(uint _id, string memory _signal) public {
        Pole storage pole = poles[_id];
        require(pole.id != 0, "Pole ID does not exist"); // Check if the pole exists
        pole.signal = _signal;
        pole.lastUpdated = block.timestamp;
        emit SignalChanged(_id, _signal, block.timestamp);
    }
}
