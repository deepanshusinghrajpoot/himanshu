import React, { useContext, useState } from 'react'
import { AppContext } from '../../../context/AppContext';

const UseStateExample3 = () => {

    const data = useContext(AppContext);

    const [count, setCount] = useState(0);
    
    const increaseCount = () => {
        setCount(prev=> prev + 1);  // 0 + 1 = 1
        setCount(prev=> prev + 1);  // 1 + 1 = 2
        setCount(prev=> prev + 1);  // 2 + 1 = 3
        setCount(prev=> prev + 1);  // 3 + 1 = 4
    }
    const decreaseCount = () => {
        setCount(count - 1);  // 0 - 1 = -1
        setCount(count - 1);  // 0 - 1 = -1
        setCount(count - 1);  // 0 - 1 = -1
        setCount(count - 1);  // 0 - 1 = -1
    }

  return (
    <div>
          <p>Count: {count}</p>
          <button onClick={increaseCount} >Increase Count</button>
          <button onClick={decreaseCount} >Decrement Count</button>
          <h4>Phone:{data.phone}</h4>
          <h4>Name:{data.owner}</h4>
    </div>
  )
}

export default UseStateExample3