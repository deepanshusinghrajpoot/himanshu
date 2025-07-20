import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { decrement, getUserAccount, increment, incrementByAmount } from '../slices/accountSlices';





const Account = () => {



      // here react not render the this dynamic value because {store.getState().bonus.points} because react render dynamic value when change the state
      // So, this problem is solve by :- react-redux libraries
      
      // react-redux is give easy access of the the this store and store have getState() and dispatch()

      // react-redux merge the state of react and redux

      // react-redux do only three things:-  (first:- use Provider, second:- use:- useDispatch(), useSelector() )
      
      


  const dispatch = useDispatch();

  const [value, setValue] = useState();

  const amount = useSelector((state)=> state.account.amount)
  const points = useSelector((state)=>state.bonus.points);



  return (
    <div>
        <h1>Account Component</h1>
        <div>
            <h3>Amount:${amount}</h3>
            <h3>Points:${points}</h3>
            <button onClick={()=> dispatch(increment())} >Increment +</button>
            <button onClick={()=> dispatch(decrement())} >Decrement -</button>
            <input placeholder='Inter a number....' type="number" value={value} onChange={(e)=>setValue(+e.target.value)} />
            <button onClick={()=> dispatch(incrementByAmount(value))} >Increment By {value}+</button>
            <button onClick={()=> dispatch(getUserAccount(425525))} >Get User</button>
        </div>
    </div>
  )
}

export default Account