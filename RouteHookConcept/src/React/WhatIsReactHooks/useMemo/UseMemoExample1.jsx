import React, { useContext, useMemo, useState } from 'react'
import { AppContext } from '../../../context/AppContext';

const UseMemoExample1 = () => {

  
  const data = useContext(AppContext);

  
  const [number, setNumber] = useState(0);
  const [count, setCount] = useState(0);

  const cubNum = (num)=>{
    console.log("Calculation Done!");
    return Math.pow(num, 3);
  }
  
  // The useMemo Hook only runs when one of its dependencies gets updated
  // If we not provided dependecies variable then useMemo function not run
  const result = useMemo(()=>{
   return cubNum(number);
  },[number])    // When number get change then execute the useMemo Hook


  return (
    <div>
         <input type="number" value={number}  onChange={(e)=>setNumber(e.target.value)} />
         <p>Cube of the number:{result}</p>
         <button  onClick={()=> setCount(count + 1)} >Increase +1</button>
         <p>Counter:{count}</p>
         <h4>Phone:{data.phone}</h4>
         <h4>Name:{data.owner}</h4>
    </div>
  )
}

export default UseMemoExample1