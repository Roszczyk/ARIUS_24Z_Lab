import React from 'react';

const Task = ({ task, toggleTaskStatus, deleteTask }) => {
  const isOverdue = new Date(task.dueDate) < new Date() && task.done === 'niewykonane';

  return (
    <div className="task">
      <h2>{task.title}</h2>
      <p>{task.details}</p>
      <p>Termin: {new Date(task.deadline).toLocaleString()}</p>
      <p>Status: {isOverdue ? 'przeterminowane' : task.done}</p>
      <p>Trudność: {'★'.repeat(task.stars)}{'☆'.repeat(10 - task.stars)}</p>
      <button onClick={() => toggleTaskStatus(task.id)}>
        {task.status === 'wykonane' ? 'Oznacz jako niewykonane' : 'Oznacz jako wykonane'}
      </button>
      {(task.status === 'przeterminowane' || task.status === 'wykonane') && (
        <button onClick={() => deleteTask(task.id)}>Usuń zadanie</button>
      )}
    </div>
  );
};

export default Task;
