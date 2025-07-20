import React from 'react'
import useLocalStorage from '../../../hooks/useLocalStorage';


const CustomHookExample1 = () => {

  const [name, setName] = useLocalStorage("username", "");
  const [id, setId] = useLocalStorage("user", "");

  return (
    <div>
        <input  type="text" placeholder="Enter your name..."  value={name} onChange={(e)=> setName(e.target.value)} />
        <p>Hellow, {name} !</p>
        <input  type="text" placeholder="Enter your id..."  value={id} onChange={(e)=> setId(e.target.value)} />
        <p>Your id: {id} !</p>
    </div>
  )
}

export default CustomHookExample1