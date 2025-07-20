import React from 'react'
import UseStateExample1 from './UseStateExample1'
import UseStateExample2 from './UseStateExample2'
import UseStateExample3 from './UseStateExample3'

const UseState = () => {

  /*
    =================== useState ===================
  
    useState is a react hook, which creates an "state variable". 
    Which helps us to track state in components & updates the user information when state changes.

    const [variabale, setVariableFunction] = useState(initialValue);
  
  */

  return (
    <div> 
        <h1>================ useState Hook Example ===================</h1>
        <h3>------- Example 1 ---------</h3>
        <UseStateExample1 />
        <h3>------- Example 2 ---------</h3>
        <UseStateExample2 />
        <h3>------- Example 3 ---------</h3>
        <UseStateExample3 />
    </div>
  )
}

export default UseState