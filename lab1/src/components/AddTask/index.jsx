import React, { useState } from 'react';
import { IoIosAdd } from "react-icons/io";

export default function AddTask({onNewTask = f => f}) {
  const [title, setTitle] = useState('');
  const [details, setDetails] = useState('');
  const [deadline, setDeadline] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onNewTask(
      title,
      details,
      deadline
    );
    setTitle('');
    setDetails('');
    setDeadline('');
  };

  return (
    <dev>
    <h2>Dodaj zadanie</h2>
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Tytuł" value={title} onChange={(e) => setTitle(e.target.value)} required />
      <br/>
      <input type="text" placeholder="Szczegóły" value={details} onChange={(e) => setDetails(e.target.value)} required />
      <br/>
      <input type="datetime-local" value={deadline} onChange={(e) => setDeadline(e.target.value)} required />
      <br/>
      <button type="submit"><IoIosAdd /><br/>Dodaj zadanie</button>
    </form>
    </dev>
  );
};