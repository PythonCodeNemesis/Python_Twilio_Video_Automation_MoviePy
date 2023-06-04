import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [emailList, setEmailList] = useState('');
  const [nameList, setNameList] = useState('');
  const [message, setMessage] = useState('');

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      // Make API request to the Flask backend
      const response = await axios.post('http://localhost:5000/send-video', {
        email: emailList,
        name: nameList
      });
      setMessage(response.data.message);
      // Reset the form inputs
      setEmailList('');
      setNameList('');
    } catch (error) {
      console.error(error);
      setMessage('An error occurred while sending the video.');
    }
  };

  return (
    <div className="container">
      <form onSubmit={handleFormSubmit}>
        <div className="form-group">
          <label>Email:</label>
          <input className="form-control" type="text" value={emailList} onChange={(e) => setEmailList(e.target.value)} />
        </div>
        <div className="form-group">
          <label>Name:</label>
          <input className="form-control" type="text" value={nameList} onChange={(e) => setNameList(e.target.value)} />
        </div>
        <button className="btn btn-primary" type="submit">Submit</button>
      </form>
      {message && <p className="message">{message}</p>}
    </div>
  );
};

export default App;
