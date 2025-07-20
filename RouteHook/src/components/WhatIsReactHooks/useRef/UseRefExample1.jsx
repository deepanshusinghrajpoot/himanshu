import React, { useContext, useEffect, useRef, useState } from 'react'


const UseRefExample1 = () =>{
  
   const [value, setValue] = useState(0);
   const count = useRef(0);  // count is a object :- {current:0}
   
   
   useEffect(()=>{
     count.current = count.current + 1;
   })

  return (
     <div>
        <button onClick={()=>{setValue(prev=> prev+1)}}>Increase +1</button>
        <p>value:{value}</p>
        <button onClick={()=>{setValue(prev=> prev-1)}}>Decrease -1</button>
        <p>count:{count.current}</p>
   
     </div>
  )
}

export default UseRefExample1