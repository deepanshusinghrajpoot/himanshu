import React, { useState } from 'react'
import {increment, decrement, incrementByAmount, getUserAccount } from  '../actions/index'
import { useDispatch, useSelector } from 'react-redux'





const Account = () => {



      // here react not render the this dynamic value because {store.getState().bonus.points} because react render dynamic value when change the state
      // So, this problem is solve by :- react-redux libraries
      
      // react-redux is give easy access of the the this store and store have getState() and dispatch()

      // react-redux merge the state of react and redux

      // react-redux do only three things:-  (first:- use Provider, second:- use:- useDispatch(), useSelector() )
      
      


  const dispatch = useDispatch();

  const [value, setValue] = useState();
  const [id, setId] = useState();


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
            <input placeholder='Type a number...' type="number" value={value} onChange={(e)=>setValue(+e.target.value)} />
            <button onClick={()=> dispatch(incrementByAmount(value))} >Increment By {value}+</button>
            <input placeholder='Give the id of accound...' type="number" value={id} onChange={(e)=>setId(e.target.value)} />
            <button onClick={()=> dispatch(getUserAccount(id))} >Init Account</button>
        </div>
    </div>
  )
}

export default Account