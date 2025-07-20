import React, { useEffect, useRef, useState } from 'react'

const Ram = () => {
       const [state, setState] = useState(0);
   
       const mutableVariavel = useRef(0);
       const inputRef = useRef();
   
   
       useEffect(()=>{
         mutableVariavel.current = mutableVariavel.current  + 1;
       })
   
   
       return (
           <div>
              <button onClick={()=>setState(prev=> prev+1)} >+1</button>
              <p>{state}</p>
              <button onClick={()=>setState(prev=>prev-1)}>-1</button>
              <p>Mutable Variable :- {mutableVariavel.current}</p>
              <input type='text' ref={inputRef} />
           </div>
       )
}

export default Ram