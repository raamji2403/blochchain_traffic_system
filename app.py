from flask import Flask, jsonify, request , render_template
from web3 import Web3
import json

app = Flask(__name__)

# Connect to local Ganache blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
if w3.is_connected():
    print("Connected to Ganache")

# Load compiled contract
with open("compiled_contract.json") as file:
    compiled_contract = json.load(file)

contract_abi = compiled_contract["abi"]
contract_bytecode = compiled_contract["bytecode"]

# Set up contract (assuming it has already been deployed)
contract_address = "0x09f9AA46537f4A63561715F69191b68b6953EC98"  # Replace with actual deployed contract address
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Default account to interact with
w3.eth.default_account = w3.eth.accounts[0]

# Route to add a new traffic pole
@app.route('/add_pole', methods=['POST'])
def add_pole():
    try:
        # Interact with the smart contract's addPole() function
        tx_hash = contract.functions.addPole().transact()
        # Wait for the transaction to be mined
        w3.eth.waitForTransactionReceipt(tx_hash)
        return jsonify({"message": "Pole added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to change the signal of an existing traffic pole
@app.route('/change_signal', methods=['POST'])
def change_signal():
    data = request.json
    pole_id = data.get('pole_id')
    signal = data.get('signal')

    try:
        # Interact with the smart contract's changeSignal function
        tx_hash = contract.functions.changeSignal(pole_id, signal).transact()
        # Wait for the transaction to be mined
        w3.eth.waitForTransactionReceipt(tx_hash)
        return jsonify({"message": "Signal changed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to get all traffic poles
@app.route('/get_poles', methods=['GET'])
def get_poles():
    poles = []
    pole_count = contract.functions.poleCount().call()

    # Loop through all poles and fetch their details from the contract
    for i in range(1, pole_count + 1):
        pole = contract.functions.poles(i).call()
        poles.append({
            "id": pole[0],
            "signal": pole[1],
            "last_updated": pole[2]
        })

    return jsonify(poles)

# Serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')  # Assuming 'index.html' is the frontend HTML file



if __name__ == '__main__':
    app.run(debug=True)