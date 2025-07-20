import React, { useContext } from 'react'
import { AppContext } from '../../../context/AppContext'

const UseContextExample1 = () => {
  
  /*
    ********   1. Creating the context  *************
     Inside the context folder create context using:-  createContext()

    ********   2. Providing the context  *************
     Inside the main.jsx file wrap the App component inside the ContextProvide function
    
    ********   3. Consuming the context  *************
     Now consuming context in every component useing :-  useContext(file name of context folder);

  */




  
  const data = useContext(AppContext);

  return (
    <div>
         <h4>Phone:{data.phone}</h4>
         <h4>Name:{data.owner}</h4>
    </div>
  )
}

export default UseContextExample1