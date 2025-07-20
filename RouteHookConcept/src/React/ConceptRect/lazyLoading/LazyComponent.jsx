import React, { useState } from 'react'
import { todos } from './todos' 



const LazyComponent = () => {

  
  const [ todosList, setTodosList ] = useState(todos); 


  return (
    <div>
         <h1>LazyComponent</h1>
         <ul>
            {
                todosList.map((item)=><li key={item.id} >{item.title}</li>)
            }
         </ul>

    </div>
  )
}

export default LazyComponent