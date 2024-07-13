
# Blockchain and IoT Application

This project is a Flask-based application that integrates a simple blockchain implementation with IoT devices. The application allows the creation of new blocks, adding transactions, and capturing sensor data from IoT devices.

## Features

- **Blockchain**:
  - Create new blocks
  - Add new transactions
  - Proof of Work algorithm
  - Chain validation
- **IoT Devices**:
  - Simulate sensor data (temperature, humidity, location)
  - Capture and store sensor data as transactions in the blockchain

## Requirements

- Python 3.x
- Flask
- Flask-CORS

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:

    ```bash
    pip install Flask Flask-CORS
    ```

3. Ensure the frontend build files are placed in `./blockchain-frontend/build`.

## Running the Application

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Access the application by navigating to `http://localhost:5000` in your web browser.

## API Endpoints

### Serve Frontend

- **`GET /`**
  - Serves the frontend application from the `./blockchain-frontend/build` directory.

### Blockchain Operations

- **`GET /mine`**
  - Mines a new block and adds it to the blockchain.
  - **Response**:
    - `message`: Confirmation message
    - `index`: Index of the new block
    - `transactions`: List of transactions in the new block
    - `proof`: Proof of work for the new block
    - `previous_hash`: Hash of the previous block

- **`POST /transactions/new`**
  - Adds a new transaction to the list of transactions.
  - **Request Body**:
    - `sender`: Sender of the transaction
    - `recipient`: Recipient of the transaction
    - `amount`: Amount of the transaction
  - **Response**:
    - `message`: Confirmation message with the index of the block to which the transaction will be added

- **`GET /chain`**
  - Returns the full blockchain.
  - **Response**:
    - `chain`: List of blocks in the blockchain
    - `length`: Length of the blockchain

### IoT Operations

- **`GET /iot/capture`**
  - Captures sensor data from IoT devices and adds the data as transactions to the blockchain.
  - **Response**:
    - `message`: Confirmation message
    - `data`: List of captured sensor data

## Project Structure

```plaintext
.
├── app.py                # Main Flask application file
├── blockchain-frontend   # Frontend build files (React/Vue/Other)
│   └── build
│       └── index.html
└── README.md             # Project README file
```

## How It Works

- **Blockchain**: The `Blockchain` class implements the basic functionalities of a blockchain, including creating new blocks, adding transactions, and the proof of work algorithm.
- **IoT Devices**: The `IoTDevice` class simulates IoT devices that generate random sensor data. The `capture_data` endpoint captures data from these devices and adds it to the blockchain as transactions.
- **Flask Application**: The Flask application (`app.py`) provides the REST API endpoints to interact with the blockchain and IoT devices.

## Notes

- The project simulates IoT devices and their data. In a real-world scenario, actual IoT devices would be integrated to provide real sensor data.
- Ensure the frontend build files are properly placed in the `./blockchain-frontend/build` directory for the application to serve the frontend correctly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
