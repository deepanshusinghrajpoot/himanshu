import React, { useContext, useState } from 'react'
import { AppContext } from '../../../context/AppContext'

const UseStateExample2 = () => {


    const data = useContext(AppContext);

   

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
        <h4>{data.phone}</h4>
        <h4>{data.owner}</h4>
    </div>
  )
}

export default UseStateExample2