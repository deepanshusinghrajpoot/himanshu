import React from 'react'
import UseReducerExample1 from './UseReducerExample1'

const UseReducer = () => {
  
  /*

     =================== useReducer ===================
     
     useReducer is similar to useState, But instead of providing state & setter function.
     It provides state and dispatch function.

     
     The useReducer Hook accept two arguments
     1.- Reducer function
     2.- initial state
     and returns: Current state and Dispatch method
     So,
        
        first argument:- The reducer function specifies how the state gets updated.


  */

  return (
    <div>
        <h1>=================== useReducer Hook example ===================</h1>
        <h3>------- Example 1 ---------</h3> 
        <UseReducerExample1 />
    </div>
  )
}

export default UseReducer






