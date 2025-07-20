import React, { useContext, useState } from 'react'

const UseStateExample3 = () => {

  

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
          <button onClick={decreaseCount} ></button>
          
    </div>
  )
}

export default UseStateExample3