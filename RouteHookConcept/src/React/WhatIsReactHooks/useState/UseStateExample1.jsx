
import React, { useContext, useState } from 'react'
import { AppContext } from '../../../context/AppContext';

const UseStateExample1 = () => {


   const data = useContext(AppContext);


   const [color, setColor] = useState("red"); 
   // color:- is a variable
   // setColor:- is a fuction which is used to modify the variable.
   
   const changeColor = () => {
        setColor(color === "red" ? "blue" : "red");
   }

  return (
    <div>
        <p>My fevourite color is {color}!</p>
        <button onClick={changeColor} >{ color==="red"? "blue" : "red" }</button>
        <h4>Phone:{data.phone}</h4>
        <h4>Name:{data.owner}</h4>
    </div>
  )
}

export default UseStateExample1
