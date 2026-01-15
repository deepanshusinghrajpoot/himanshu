import React, { useCallback, useContext, useState } from 'react'
import Header1 from './Header1';
import Header2 from './Header2';
import Header3 from './Header3';
import { AppContext } from '../../../context/AppContext';
import Header4 from './Header4';

const UseCallbackExapmle1 = () => {

  /*

     useCallback is a React Hook that lets you cache a function definition between re-renders.
     If dependencies not provide then it will not create new function (That mean it use cach function)
     If dependencies change then it create a new function

  */


  
  const data = useContext(AppContext);

 
  const [count, setCount] = useState(0);


  const newFunction1 = () => {} // when change the count then render component then create new instance of this function 
                         // So header1 render  when change the count

  
  
  const newFunction2 = useCallback(()=>{})

  // If we not provided dependecies variable then useCallback function not create new intence of function
  // So, header2 not render when chage the state in the UseCallbackExapmle1(component) 
  const newFunction3 = useCallback(()=> {}, [])



  // If we provided dependecies variable then useCallback function create new intence of function when change the dependecie variable
  // So, header3 render when chage the count
  const newFunction4 = useCallback(()=> {}, [count])

  return (
    <div>
         <Header1 newFunction={newFunction1} />
         <Header2 newFunction={newFunction2} />
         <Header3 newFunction={newFunction3} />
         <Header4 newFunction={newFunction4}/>
         <button onClick={()=>setCount(prev=>prev+1)} >Increase +1</button>
         <p>Counter:{count}</p>
         <h4>Phone:{data.phone}</h4>
         <h4>Name:{data.owner}</h4>
    </div>
  )
}

export default UseCallbackExapmle1