import React, { useState } from 'react';

const AddTask = ({ addTask }) => {
  const [title, setTitle] = useState('');
  const [details, setDetails] = useState('');
  const [deadline, setDeadline] = useState('');
  const [difficulty, setDifficulty] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    addTask({
      title,
      details,
      deadline,
      done: 'niewykonane',
      difficulty: parseInt(difficulty, 10)
    });
    setTitle('');
    setDetails('');
    setDeadline('');
    setDifficulty(0);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Tytuł" value={title} onChange={(e) => setTitle(e.target.value)} required />
      <input type="text" placeholder="Szczegóły" value={details} onChange={(e) => setDetails(e.target.value)} required />
      <input type="datetime-local" value={deadline} onChange={(e) => setDeadline(e.target.value)} required />
      <input type="number" min="0" max="10" value={difficulty} onChange={(e) => setDifficulty(e.target.value)} required />
      <button type="submit">Dodaj zadanie</button>
    </form>
  );
};

export default AddTask;
