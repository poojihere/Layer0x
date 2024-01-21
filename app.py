# Install necessary packages
# pip install Flask pymongo requests aiohttp

from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import aiohttp
import asyncio

import requests

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/blockchain_api'
mongo = PyMongo(app)

# Check if the connection to MongoDB is successful
with app.app_context():
    try:
        if mongo.db is not None:
            print("Connected to MongoDB successfully.")
        else:
            print("Error: Could not connect to MongoDB.")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

# Define the blockchain collection in MongoDB
blockchain_collection = mongo.db.blockchains

# CRUD Operations for Blockchains
@app.route('/blockchains', methods=['GET', 'POST'])
def blockchains():
    if request.method == 'GET':
        # Retrieve all blockchains
        blockchains_list = blockchain_collection.find()
        blockchains = []
        for blockchain in blockchains_list:
            blockchains.append({
                'name': blockchain['name'],
                'status': blockchain['status'],
                'rpc_endpoint': blockchain.get('rpc_endpoint', 'N/A')
            })
        return jsonify({'blockchains': blockchains})

    elif request.method == 'POST':
        # Add a new blockchain or update an existing one
        data = request.get_json()
        name = data.get('name')
        status = data.get('status')
        rpc_endpoint = data.get('rpc_endpoint')

        if not name or not status or not rpc_endpoint:
            return jsonify({'error': 'Name, status, and RPC endpoint are required'}), 400

        try:
            existing_blockchain = blockchain_collection.find_one({'name': name})
            if existing_blockchain:
                # Update existing blockchain
                blockchain_collection.update_one(
                    {'name': name},
                    {'$set': {'status': status, 'rpc_endpoint': rpc_endpoint}}
                )
            else:
                # Insert new blockchain
                blockchain_collection.insert_one({
                    'name': name,
                    'status': status,
                    'rpc_endpoint': rpc_endpoint
                })

            return jsonify({'message': 'Blockchain added/updated successfully'}), 201
        except Exception as e:
            print(f"Error adding blockchain to MongoDB: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

# Status Endpoint for all blockchains
@app.route('/status', methods=['GET'])
async def status():
    # Fetch required info of all blockchains
    blockchains_list = blockchain_collection.find()
    status_info = []

    async def fetch_blockchain_status(session, rpc_endpoint, name):
        try:
            async with session.get(f'{rpc_endpoint}/getinfo') as response:
                if response.status == 200:
                    blockchain_info = await response.json()
                    return {
                        'name': name,
                        'status': 'Online',
                        'block_height': blockchain_info.get('blocks', 0)
                    }
                else:
                    return {'name': name, 'status': 'Offline', 'block_height': 0}
        except Exception as e:
            return {'name': name, 'status': 'Error', 'block_height': 0, 'error_message': str(e)}

    async def fetch_all_blockchain_statuses():
        async with aiohttp.ClientSession() as session:
            tasks = [
                fetch_blockchain_status(session, blockchain.get('rpc_endpoint'), blockchain['name'])
                for blockchain in blockchains_list
            ]
            return await asyncio.gather(*tasks)

    status_info = await fetch_all_blockchain_statuses()

    response = {
        'success': True,
        'result': status_info
    }

    return jsonify(response)

# Function to get the status of a blockchain using its RPC endpoint
def get_blockchain_status(rpc_endpoint):
    try:
        response = requests.get(f'{rpc_endpoint}/getinfo', timeout=5)
        if response.status_code == 200:
            blockchain_info = response.json()
            return {
                'status': 'Online',
                'block_height': blockchain_info.get('blocks', 0)
            }
        else:
            return {'status': 'Offline', 'block_height': 0}
    except requests.RequestException as e:
        return {'status': 'Error', 'block_height': 0, 'error_message': str(e)}

# Landing page with information about the API
@app.route('/')
def landing_page():
    return render_template('landing_page.html')

if __name__ == '__main__':
    app.run(debug=True)
