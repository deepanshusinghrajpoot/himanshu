
import React, { useContext, useState } from 'react'

const UseStateExample1 = () => {





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
    </div>
  )
}

export default UseStateExample1
