import React from 'react'
import UseCallbackExapmle1 from './UseCallbackExapmle1'

const UseCallback = () => {

   /*
     =================== useCallback ===================

     useCallback React Hook that lets you/we cache a function definition between re-renders. 

     It means, when we use the useCallback Hook, it doesn't create multiple instance of same function when re-render happens.

     Instead of creating new instance of the function, it provides the cached function on re-render of the component.
  */



  return (
    <div>
         <h1>=================== useCallback Hook example ===================</h1>
         <h3>------- Example 1 ---------</h3> 
         <UseCallbackExapmle1 />

    </div>
  )
}

export default UseCallback