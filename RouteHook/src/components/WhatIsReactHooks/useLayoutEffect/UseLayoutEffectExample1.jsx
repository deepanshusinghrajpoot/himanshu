import React, { useEffect, useLayoutEffect } from 'react'

const UseLayoutEffectExample1 = () => {  

 /*
    in console print 
    first:- Message from useLayoutEffect
    second:- Message from useEffect

    because first useLayoutEffect function execute when reload page then render DOM element and after execute the useEffect Hook


    *** react official document says useLayoutEffect can heart the performance of app 
    so, recommended to use useEffect Hook when possible

     
 */
  

  useEffect(()=>{
     console.log("Message from useEffect");
  },[])

  useLayoutEffect(()=>{
     console.log("Message from useLayoutEffect");
  },[])

  return (
    <div>
         <p>Test useLayoutEffect Hook with console</p>
    </div>
  )
}

export default UseLayoutEffectExample1