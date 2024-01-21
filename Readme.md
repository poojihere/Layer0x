# Blockchain Status API

## Overview

This API is designed to monitor and manage the status of various blockchains. Each blockchain is identified by its name and has its own RPC endpoint, providing information about its current status, whether it's running, and the current block height.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Endpoints](#endpoints)
  - [Example Requests](#example-requests)

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/blockchain-status-api.git

2. Install the required Python packages:
    ```bash
    pip install flask
    pip install flask_pymongo
    pip install aiohttp
    pip install asyncio
    pip install requests

3. Set up your MongoDB database.

4. Configure the MongoDB URI in app.py:
    ```bash
    app.config['MONGO_URI'] = 'mongodb://your-mongodb-uri/blockchain_api'


5. Run the file:
    ```bash
    python app.py


### Usage
## API Endpoints

- **GET /blockchains**: Retrieve information about all configured blockchains.
- **POST /blockchains**: Add or update information about a blockchain.
- **GET /blockchains/{name}**: Retrieve details of a specific blockchain by its name.
- **DELETE /blockchains/{name}**: Delete a specific blockchain by its name.
- **GET /status**: Retrieve the status of all configured blockchains.


## Example Requests

### 1. Retrieve information about all blockchains

    GET http://localhost:5000/blockchains

### 2. Add or update a blockchain
    POST http://localhost:5000/blockchains

    Content-Type: application/json

    {
    "name": "New Blockchain",
    "status": "Active",
    "rpc_endpoint": "https://example.com/rpc"
    }   

### 3. Retrieve details of a specific blockchain by its name

    GET http://localhost:5000/blockchains/{name}

### 4. Delete a specific blockchain by its name

    DELETE http://localhost:5000/blockchains/{name}

### 5.  Retrieve the status of all configured blockchains

    GET http://localhost:5000/status


## Constraints and Requirements

This API satisfies the below Constraints:

1. **Utilize the RPC API for each blockchain to fetch status information:**

The get_blockchain_status function in the provided code sends a request to the RPC endpoint (getinfo endpoint) of each blockchain to fetch status information.

2. **API can handle concurrent requests for multiple blockchains:**

- The status endpoint is now defined with the async keyword, indicating that it contains asynchronous code.
- The fetch_blockchain_status function uses aiohttp to make an asynchronous HTTP request to each blockchain's RPC endpoint.
- The fetch_all_blockchain_statuses function asynchronously gathers the status information for all blockchains concurrently.
- The asyncio.gather function is used to run multiple asynchronous tasks concurrently.
- The await keyword is used to wait for the results of asynchronous tasks.


3. **Implement error handling to manage cases where a blockchain is not reachable or returns an error response:**
    
    The get_blockchain_status function does include a basic try-except block for handling exceptions. It catches general exceptions and returns an error status if an exception occurs during the request to the RPC endpoint. However, you may want to enhance error handling to differentiate between various types of errors (e.g., connection errors, timeout errors) and provide more detailed error messages in the response.

4. **API Documentation Using Swagger Hub Link:**

    https://app.swaggerhub.com/apis/B182782/Blockchain_montior_api_documentation/1.0.0




