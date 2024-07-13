import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [output, setOutput] = useState('');
  const [sender, setSender] = useState('');
  const [recipient, setRecipient] = useState('');
  const [amount, setAmount] = useState('');

  const mineBlock = async () => {
    try {
      const response = await axios.get('http://localhost:5000/mine');
      setOutput(JSON.stringify(response.data, null, 4));
    } catch (error) {
      console.error("Error mining block:", error);
      setOutput('Error mining block');
    }
  };

  const captureData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/iot/capture');
      setOutput(JSON.stringify(response.data, null, 4));
    } catch (error) {
      console.error("Error capturing data:", error);
      setOutput('Error capturing data');
    }
  };

  const viewChain = async () => {
    try {
      const response = await axios.get('http://localhost:5000/chain');
      setOutput(JSON.stringify(response.data, null, 4));
    } catch (error) {
      console.error("Error viewing chain:", error);
      setOutput('Error viewing chain');
    }
  };

  const submitTransaction = async (event) => {
    event.preventDefault();
    const transactionData = {
      sender: sender,
      recipient: recipient,
      amount: amount
    };
    try {
      const response = await axios.post('http://localhost:5000/transactions/new', transactionData);
      setOutput(JSON.stringify(response.data, null, 4));
    } catch (error) {
      console.error("Error submitting transaction:", error);
      setOutput('Error submitting transaction');
    }
  };

  return (
    <div className="App">
      <h1>Blockchain IoT</h1>
      <button onClick={mineBlock}>Mine Block</button>
      <button onClick={captureData}>Capture IoT Data</button>
      <button onClick={viewChain}>View Blockchain</button>

      <form onSubmit={submitTransaction}>
        <h2>Submit New Transaction</h2>
        <input
          type="text"
          placeholder="Sender"
          value={sender}
          onChange={(e) => setSender(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Recipient"
          value={recipient}
          onChange={(e) => setRecipient(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          required
        />
        <button type="submit">Submit Transaction</button>
      </form>

      <pre>{output}</pre>
    </div>
  );
}

export default App;
