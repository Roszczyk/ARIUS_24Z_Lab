import React, { useState, useEffect } from 'react';
import TaskList from './components/TaskList';
import tasksData from './source_data/todo.json';

function App(){
  const [tasks, setTasks] = useState(tasksData);
  return(
    <TaskList 
      tasks = {tasks}
      onRemoveTask = {id => {
        const newTaskList = tasks.filter(task => task.id !== id);
        setTasks(newTaskList);
      }}
      onRateTask = {(id, stars) => {
        const newTaskList = tasks.map(task =>
          task.id === id ? {...task, stars} : task);
        setTasks(newTaskList);
      }}
    />
  );
}

export default App;