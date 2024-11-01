import React from 'react';
import Task from '../Task';

export default function TaskList({tasks = [], onRemoveTask = f => f, onRateTask = f => f})
{
  if(!tasks.length) return <div>Brak zadań do zrobienia.</div>;
  return (
    <div className="task-list">
      <h1>Lista Zadań do wykonania:</h1>
      {
        tasks.map(task => <Task 
          key={task.id} 
          {...task} 
          onRemove = {onRemoveTask}
          onRate = {(id, stars) => onRateTask(id, stars)}
        />)
      }
    </div>
  );
}
