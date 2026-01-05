import React from 'react'
import UseRefExample1 from './UseRefExample1'
import UseRefExample2 from './useRefExample2'

const UseRef = () => {

  /*


       =================== useState ===================
       useRef react Hook that allow us to create mutable variable,
       which will not re-render the component.

       It means when we use to create a variable using useRef and when variable value changes then it will not re-render the component

       - useRef is also used for accessing DOM elements.



  */  
 

  return (

   <div>
       <h1>=================== useRef Hook example ===================</h1>
       <h3>------- Example 1 ---------</h3>
       <UseRefExample1 />
       <h3>------- Example 2 ---------</h3>
       <UseRefExample2 />
   </div>
   
  )
}

export default UseRef