from flask import Flask, jsonify, request, send_from_directory
import hashlib
import json
from time import time
import random
from flask_cors import CORS
import os

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

class IoTDevice:
    def __init__(self, device_id):
        self.device_id = device_id

    def capture_data(self):
        return {
            'device_id': self.device_id,
            'temperature': random.uniform(10.0, 30.0),
            'humidity': random.uniform(20.0, 50.0),
            'location': f'{random.uniform(-90.0, 90.0)}, {random.uniform(-180.0, 180.0)}'
        }

app = Flask(__name__, static_folder='./blockchain-frontend/build', static_url_path='/')
CORS(app) 
blockchain = Blockchain()
devices = [IoTDevice(device_id=f'device_{i}') for i in range(5)]

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/mine', methods=['GET'])
def mine():
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


@app.route('/iot/capture', methods=['GET'])
def capture_data():
    sensor_data = []
    for device in devices:
        data = device.capture_data()
        blockchain.new_transaction(sender='farmer', recipient='distributor', amount=json.dumps(data))
        sensor_data.append(data)

    response = {
        'message': 'Sensor data captured and transactions added',
        'data': sensor_data
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
