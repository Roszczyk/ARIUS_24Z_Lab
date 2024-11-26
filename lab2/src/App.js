import React from 'react';
import './App.css';
import { FetchData } from './components/FetchData';
import List from "./components/List";


function App() {
  const images = FetchData();
  const renderItem = item => (
    <div style={{display: "flex"}}>
      <img src={item.url} alt={item.id} width={100} height={100} />
      <pre>ID: {item.id}<br />width: {item.width}</pre>
    </div>
  );

  return (
    <List data={images} renderItem = {renderItem}/>
  )
}

export default App;