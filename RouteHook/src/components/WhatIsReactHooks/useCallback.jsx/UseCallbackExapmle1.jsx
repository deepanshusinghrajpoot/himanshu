import React, { useCallback, useContext, useState } from 'react'
import Header1 from './Header1';
import Header2 from './Header2';
import Header3 from './Header3';


const UseCallbackExapmle1 = () => {

  /*

     useCallback is a React Hook that lets you cache a function definition between re-renders.
     If dependencies not provide then it will not create new function (That mean it use cach function)
     If dependencies change then it create a new function

  */


 
  const [count, setCount] = useState(0);


  const newFunction1 = () => {} // when change the count then render component then create new instance of this function 
                         // See console 


  // If we not provided dependecies variable then useCallback function not create new function
  // So, header2 not render when chage the state in the UseCallbackExapmle1(component) 
  const newFunction2 = useCallback(()=> {}, [])



  // If we provided dependecies variable then useCallback function create new function when change the dependecie variable
  // So, header3 render when chage the count
  const newFunction3 = useCallback(()=> {}, [count])

  return (
    <div>
         <Header1 newFunction={newFunction1} />
         <Header2 newFunction={newFunction2} />
         <Header3 newFunction={newFunction3} />
         <button onClick={()=>setCount(prev=>prev+1)} >Increase +1</button>
         <p>Counter:{count}</p>
    </div>
  )
}

export default UseCallbackExapmle1