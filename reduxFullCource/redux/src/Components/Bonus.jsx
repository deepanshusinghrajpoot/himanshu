import React from 'react'
import { incrementBonus } from '../actions';

const Bonus = ({store}) => {
    

      // here react not render the this dynamic value because {store.getState().bonus.points} because react render dynamic value when change the state
      // So, this problem is solve by :- react-redux libraries
      
      // react-redux is give easy access of the the this store and store have getState() and dispatch()




      return (
        <div>
            <div>
                 <h1>Bonus Component</h1>
                 <h3>Total point : {store.getState().bonus.points}</h3>
                 <button onClick={()=> store.dispatch(incrementBonus())} >Increment +</button>
            </div>
        </div>
      )
}

export default Bonus



