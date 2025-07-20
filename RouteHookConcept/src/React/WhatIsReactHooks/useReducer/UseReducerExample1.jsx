import React, { useContext, useReducer } from 'react'
import { AppContext } from '../../../context/AppContext';

const UseReducerExample1 = () => {
  
  /*
     when use useState then it is contain state and setter function:- eg: const [state, setState] = useSate(initial State)
     when use useReducer then it is contain state and dispatch method :- eg: const [state, dispatch] = useReducer(reducer, initialState)


     when we use useState then directly update the state variable using setter function
     but we use useReducer hook efficiently update the state variable for different action

  */

  const {phone, owner} = useContext(AppContext);


   
  const initialState = {count: 0};
  
  // reducer function contain two parameter :- 1. state, 2. action
  const reducer = (state, action) => {
     
     switch(action.type){
        case "increase" : {
           return {count: state.count + 1}
        }
        case "decrease" : {
           return {count: state.count - 1}
        }
        case "input" : {
           return {count: action.payoad}
        }
        default: {
            return state
        }
     }
     
  }

  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
         <p>Count:{state.count}</p>
         <button onClick={()=> dispatch({type:"increase"})}>Increase +1</button>
         <button onClick={()=> dispatch({type:"decrease"})}>Decrease -1</button>
         <br/>
         <input type="number" value={state.count} onChange={(e)=>dispatch({type:"input", payoad:Number(e.target.value)})}/>
         <h4>Phone:{phone}</h4>
         <h4>Name:{owner}</h4>
    </div>
  )
}

export default UseReducerExample1