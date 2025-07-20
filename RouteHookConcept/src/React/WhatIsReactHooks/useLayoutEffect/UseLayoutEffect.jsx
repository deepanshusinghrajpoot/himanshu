import React from 'react'
import UseLayoutEffectExample1 from './UseLayoutEffectExample1'

const UseLayoutEffect = () => {
  /*
      =================== useLayoutEffect ===================

      useLayoutEffect react hook similarly to useEffect, but it is called before
      the User Interface gets mounted.

      It's mean
      useEffect reactHook gets called after printing the DOM elements.
      but
      useLayoutEffect reactHook gets called before printing the DOM elements.


      for example
      If you create layout using DOM element and want to change the layout color using useEffect
      then first display DOM element and after it will change color of DOM element.

      If you create layout using DOM element and want to change the layout color using useLayoutEffect
      then first change color of DOM element and after display DOM element.
  */


  return (
    <div>
         <h1>=================== useLayoutEffect Hook example ===================</h1>
         <h3>------- Example 1 ---------</h3> 
         <UseLayoutEffectExample1 />
    </div>
  )
}

export default UseLayoutEffect