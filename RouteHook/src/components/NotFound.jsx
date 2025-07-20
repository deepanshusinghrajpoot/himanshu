import React from 'react'
import { useNavigate } from 'react-router-dom'

const NotFound = () => {
 
  const navigate = useNavigate();

  return (
    <div>
        <h1>404 | Page not found.</h1>
        <br />
        <button onClick={()=>navigate('/')} >go to home</button>
    </div>
  )
}

export default NotFound