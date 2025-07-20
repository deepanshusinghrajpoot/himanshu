import React from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { increment } from '../slices/bonusSlice';

const Bonus = () => {
    

      // here react not render the this dynamic value because {store.getState().bonus.points} because react render dynamic value when change the state
      // So, this problem is solve by :- react-redux libraries
      
      // react-redux is give easy access of the the this store and store have getState() and dispatch()

      // react-redux merge the state of react and redux

      // react-redux do only three things:-  (first:- use Provider, second:- use:- useDispatch(), useSelector() )
      
      
      

      const dispatch = useDispatch();


      const amount = useSelector((state)=> state.account.amount)
      const points = useSelector((state)=>state.bonus.points);




      return (
        <div>
            <div>
                 <h1>Bonus Component</h1>
                 <h3>Total point : {points}</h3>
                 <h3>Amount : {amount}</h3>
                 <button onClick={()=>{dispatch(increment())}} >Increment +</button>
            </div>
        </div>
      )
}

export default Bonus



