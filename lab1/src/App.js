import React, { useState, useEffect } from 'react';
import TaskList from './components/TaskList';
import tasksData from './source_data/todo.json';
import AddTask from './components/AddTask';
import {v4} from "uuid";

function App(){
  const [tasks, setTasks] = useState(tasksData);
  return(
    <>
    <AddTask
      onNewTask={(title, details, deadline) => {
        const newTaskList = [
          ...tasks,
          {
            id : v4(),
            title,
            details, 
            deadline,
            status : "niewykonane",
            stars : 0
          }
        ];
        setTasks(newTaskList);
      }} 

    />
      
    <TaskList
      tasks={tasks}
      onRemoveTask={id => {
        const newTaskList = tasks.filter(task => task.id !== id);
        setTasks(newTaskList);
      } }
      onRateTask={(id, stars) => {
        const newTaskList = tasks.map(task => task.id === id ? { ...task, stars } : task);
        setTasks(newTaskList);
      } }
      onChangeStatusTask={id => {
        const newTaskList = tasks.map(task => task.id === id
          ? { ...task, status: task.status === "niewykonane" ? "wykonane" : "niewykonane" }
          : task
        );
        setTasks(newTaskList);
      } } />
    </>
  );
}

export default App;