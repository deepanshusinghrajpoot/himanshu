import React, { useContext, useMemo, useState } from 'react'


const UseMemoExample1 = () => {

  
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
  },[])


  return (
    <div>
         <input type="number" value={number}  onChange={(e)=>setNumber(e.target.value)} />
         <p>Cube of the number:{result}</p>
         <button  onClick={()=> setCount(count + 1)} >Increase +1</button>
         <p>Counter:{count}</p>
         
    </div>
  )
}

export default UseMemoExample1