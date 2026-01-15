import React, { useContext, useEffect, useState } from 'react'
import { AppContext } from '../../../context/AppContext';

const UseEffectExample1 = () => {
  
 /*
   first useEffect:-  In this example useEffect use without dependencies array So, it is allow to perform side effect again and again when change any state in the component(UseEffectExample1)
   second useEffect:- In this example useEffect use with empty dependencies array So, it is allow to perform side effect only one time when change any state in the component(UseEffectExample1)
 */


  const data = useContext(AppContext);


  const [count, setCount] = useState(0);
  const [num, setNum] = useState(0);
  const [numCount, setNumCount] = useState(0);

  // Here use useEffect without dependencies array
  // So, Whenever we use useEffect without any dependencies array then it will execute callback function whenever any *state and props change in this component(UseEffectExample1) and also when load the component.
  useEffect(()=>{
    setTimeout(()=>{
      setCount((prev)=> prev+1);
    }, 2000);
  })


  // Here use useEffect with empty dependencies array
  // So, Whenever we use useEffect with empty dependencies array then it will execute callback function only one times when component(UseEffectExample1) loaded. ❌ Does not execute on state or prop changes.
  useEffect(()=>{
    setTimeout(()=>{
      setNum((prev)=> prev+1)
    },2000)
  },[])
 
  
  // Here use useEffect with nonempty dependencies array
  // So, Whenever use useEffect with nonempty dependencies array then it will execute callback function whenever any change occour in the variable of dependencies array and also when the component loaded(UseEffectExample1)
  useEffect(()=>{
    setTimeout(()=>{
      setNumCount((prev)=> prev+1)
    },2000)
  },[numCount])

  return (
    <div>
         <p>I'v rendered {count} count!</p>
         <p>I'v rendered {num} number!</p>
         <p>I'v rendered {numCount} number count!</p>
         <h4>Phone:{data.phone}</h4>
         <h4>Name:{data.owner}</h4>
    </div>
  )
}

export default UseEffectExample1