import React, { useContext, useState } from 'react'


const UseStateExample2 = () => {

   

    const [color, setColor] = useState({
        name:"Deepanshu Singh",
        age:"20",
        DOB:"20-02-2004",
        color:"red",
    })

    const changeColorHandler =()=> {
        setColor((prev)=> ({ ...prev, color:prev.color==="red" ? "blue" : "red"}));
    }


  return (
    <div>
        <p>my name is {color.name}.</p>
        <p>my age is {color.age}</p>
        <p>my DOB is {color.DOB}</p>
        <p>this color change by button {color.color}</p>
        <button onClick={changeColorHandler} >{color.color==="red"? "blue" : "red"}</button>
    </div>
  )
}

export default UseStateExample2