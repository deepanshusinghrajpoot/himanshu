import React from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { increment, incrementByAmount } from '../reducers/reward';

const Reward = () => {
    

      // here react not render the this dynamic value because {store.getState().bonus.points} because react render dynamic value when change the state
      // So, this problem is solve by :- react-redux libraries
      
      // react-redux is give easy access of the the this store and store have getState() and dispatch()

      // react-redux merge the state of react and redux

      // react-redux do only three things:-  (first:- use Provider, second:- use:- useDispatch(), useSelector() )
      
      
      

      const dispatch = useDispatch();



      const reward = useSelector((state)=>state.reward.rewards);



      return (
        <div>
            <div>
                 <h1>Reward Component</h1>
                 <h3>Total reward : {reward}</h3>
                 <button onClick={()=>{dispatch(increment())}} >Increment +</button>
                 <button onClick={()=> dispatch(incrementByAmount(7))} >IncrementByAmount 7+</button>
            </div>
        </div>
      )
}

export default Reward



