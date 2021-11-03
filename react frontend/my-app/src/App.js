import React, {useState} from 'react';
import './App.css';
import Login from './components/Login';
import Quote from './components/quote';

function App() {

  const[token, setToken] = useState('');

  const userLogin = (tok) => {
    setToken(tok);
  }

  return (
    <div className="App">
      <Login userLogin={userLogin} />
      <Quote token={token} />
    </div>
  );
}

export default App;
