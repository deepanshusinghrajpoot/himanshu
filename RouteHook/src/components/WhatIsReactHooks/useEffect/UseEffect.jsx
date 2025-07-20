import React from 'react'
import UseEffectExample1 from './UseEffectExample1'


const UseEffect = () => {

    /*
         =================== useEffect ===================

         The useEffect Hook allows you to perform side effects in your components.

         Some example of side effects are:
           - Fetching data from API
           - Directly updating the DOM
           - Timers like SetTimeOut  and SetInterval


         useEffect(callBackFunction, dependenciesArray);

         - here callBackFunction is requuired
         - and dependenciesArray is optional

    */

  return (

    <div>
         <h1>================ useEffect Hook Example ===================</h1>
         <h3>------- Example 1 ---------</h3>
         <UseEffectExample1 />
         
    </div>
  )
}

export default UseEffect