import React, { useContext, useRef } from 'react'
import { AppContext } from '../../../context/AppContext';
import { useState } from 'react';

const UseRefExample2 = () => {

  /*
      thin is another example to eccess DOM element 

      - useRef is also used for accessing DOM elements.
  */


  const data = useContext(AppContext);


  const inputElem = useRef();

  const btnHandler = () => {
    console.log(inputElem);  // {current: input}
    console.log(inputElem.current); // <input type="text" />
    inputElem.current.style.background = "blue";
  
  }


  return (
    <div>
         <input type="text" ref={inputElem} />
         <button onClick={btnHandler} >Click Here</button>
         <h4>Phone:{data.phone}</h4>
         <h4>Name:{data.owner}</h4>
    </div>
  )
}






export default UseRefExample2
