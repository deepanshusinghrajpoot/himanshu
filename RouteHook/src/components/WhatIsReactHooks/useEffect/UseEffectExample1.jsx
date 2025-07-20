import React, { useContext, useEffect, useState } from 'react'


const UseEffectExample1 = () => {
  
 /*
   first useEffect:-  In this example useEffect use without dependencies array So, it is allow to perform side effect again and again when change any state in the component(UseEffectExample1)
   second useEffect:- In this example useEffect use with empty dependencies array So, it is allow to perform side effect only one time when change any state in the component(UseEffectExample1)
 */





  const [count, setCount] = useState(0);
  const [num, setNum] = useState(0);
  const [numCount, setNumCount] = useState(0);

  // Here use useEffect without dependencies array
  // So, Whenever use useEffect without any dependencies array then it will execute this function whenever any *state change in this component(UseEffectExample1)
  useEffect(()=>{
    setTimeout(()=>{
      setCount((prev)=> prev+1);
    }, 2000);
  })


  // Here use useEffect with empty dependencies array
  // So, Whenever use useEffect with empty dependencies array then it will execute only one times this function whenever any *state change in this component(UseEffectExample1)
  useEffect(()=>{
    setTimeout(()=>{
      setNum((prev)=> prev+1)
    },2000)
  },[])
 
  
  // Here use useEffect with nonempty dependencies array
  // So, Whenever use useEffect with nonempty dependencies array then it will execute this function whenever any change in the dependencies array variable and when the component loaded(UseEffectExample1)
  useEffect(()=>{
    setTimeout(()=>{
      setNumCount((prev)=> prev+1)
    },2000)
  },[count])

  return (
    <div>
         <p>I'v rendered {count} count!</p>
         <p>I'v rendered {num} number!</p>
         <p>I'v rendered {numCount} number count!</p>
    </div>
  )
}

export default UseEffectExample1