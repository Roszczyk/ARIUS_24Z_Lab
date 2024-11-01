import React, { useState, useEffect } from 'react';
import TaskList from './components/TaskList';
import tasksData from './source_data/todo.json';

function App(){
  const [tasks, setTasks] = useState(tasksData);
  console.log(tasks);
  return(
    <TaskList 
      tasks = {tasks}
      onRemoveTask = {id => {
        const newTaskList = tasks.filter(task => task.id !== id);
        setTasks(newTaskList);
      }}
    />
  );
}

export default App;