import React, { useState, useEffect } from "react";
import axios from "axios";

const API_URL = "https://expense-tracker-a1xt.onrender.com"; // Replace with actual backend URL

const App = () => {
  const [expenses, setExpenses] = useState([]);
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    fetchExpenses();
  }, []);

  const fetchExpenses = async () => {
    const response = await axios.get(`${API_URL}/expenses`);
    setExpenses(response.data);
  };

  const addExpense = async () => {
    await axios.post(`${API_URL}/add-expense`, {
      amount,
      category,
      description,
    });
    setAmount("");
    setCategory("");
    setDescription("");
    fetchExpenses();
  };

  return (
    <div>
      <h2>Expense Tracker</h2>
      <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount" />
      <input type="text" value={category} onChange={(e) => setCategory(e.target.value)} placeholder="Category" />
      <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description" />
      <button onClick={addExpense}>Add Expense</button>
      <ul>
        {expenses.map((expense, index) => (
          <li key={index}>{expense[1]} - ${expense[0]} ({expense[2]})</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
