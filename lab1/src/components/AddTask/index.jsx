import React, { useState } from 'react';

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
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Tytuł" value={title} onChange={(e) => setTitle(e.target.value)} required />
      <input type="text" placeholder="Szczegóły" value={details} onChange={(e) => setDetails(e.target.value)} required />
      <input type="datetime-local" value={deadline} onChange={(e) => setDeadline(e.target.value)} required />
      <button type="submit">Dodaj zadanie</button>
    </form>
  );
};