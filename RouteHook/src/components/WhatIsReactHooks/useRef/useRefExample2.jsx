import React, { useContext, useRef } from 'react'


const UseRefExample2 = () => {

  /*
      thin is another example to eccess DOM element 

      - useRef is also used for accessing DOM elements.
  */

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
        
    </div>
  )
}

export default UseRefExample2