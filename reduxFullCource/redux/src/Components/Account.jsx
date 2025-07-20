import React, { useState } from 'react'

const Account = () => {

  const [account, setAccount] = useState({amount:0});
  const [value, setValue] = useState(0);

  const increment = () => {
     return setAccount({amount:account.amount + 1});
  }
  const decrement = () => {
     return setAccount({amount:account.amount - 1})
  }
  const incrementByValue = (value) => {
    return setAccount({amount:account.amount + value});
  }



  return (
    <div>
        <h1>Account Component</h1>
        <div>
            <h3>Amount:${account.amount}</h3>
            <button onClick={increment} >Increment +</button>
            <button onClick={decrement} >Decrement -</button>
            <input type="number" value={value} onChange={(e)=>setValue(+e.target.value)} />
            <button onClick={()=> incrementByValue(value)} >Increment By {value}+</button>
        </div>
    </div>
  )
}

export default Account