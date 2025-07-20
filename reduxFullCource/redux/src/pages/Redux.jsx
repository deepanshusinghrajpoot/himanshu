import React from 'react'
import { applyMiddleware, createStore, combineReducers } from "redux";
import logger from "redux-logger";
import axios from "axios";
import {thunk} from "redux-thunk";


const Redux = () => {

  
// action name constants
// const INIT = "account/init";
const INCREMENT = "account/increment";
const DECREMENT = "account/decrement";
const INCREMENT_BY_AMOUNT = "account/incrementByAmount";
const GET_ACC_USER_PENDING = "account/getUser/pending";
const GET_ACC_USER_FULFILLED = "account/getUser/fulfilled";
const GET_ACC_USER_REJECTED = "account/getUser/rejected";



const INCREMENT_BONUS = "bonus/increment";









// create store  
// createStore this liberary is deprecated in redux toolkit
// use configureStore instead of createStore
const store = createStore(
    combineReducers({
        account: accountReducer,
        bonus: bonusReducer,
    }),
    applyMiddleware(logger, thunk)

); // applyMiddleware is used to add middleware to the store, in this case, we are using logger middleware to log the actions and state changes to the console.










const history = [];



const fetchData = async()=>{
    const {data} = await axios.get("http://localhost:3000/account/1");
   // console.log(data);
}
//fetchData();







// reducer is a function that takes the current state and an action as arguments and returns a new state. It is a pure function, meaning it does not modify the original state but creates a new one based on the action received.
function accountReducer(state={amount:1}, action) {
    
    //immutablility :- it is not a good practice to mutate the state directly
    // state.amount = state.amount + 1;
    switch(action.type){
        case GET_ACC_USER_FULFILLED:
            return {amount: action.payload, pending:false }
        case GET_ACC_USER_REJECTED:
            return {...state, error:action.error, pending:false }
        case GET_ACC_USER_PENDING:
            return {...state, pending:true}
        case INCREMENT:
            return {amount: state.amount + 1}; // create a new object with the updated value
        case DECREMENT:
            return {amount: state.amount - 1}; // create a new object with the updated value
        case INCREMENT_BY_AMOUNT:
            return {amount: state.amount + action.payload}; // create a new object with the updated value
        default:
            return state;
    }

}


function bonusReducer(state = { points: 1 }, action ){
    switch(action.type){
        case INCREMENT_BONUS :
             return {points: state.points + 1}
        case INCREMENT_BY_AMOUNT : 
             if(action.payload >= 100)
                 return {points: state.points + 1}
        default:
             return state;
    }
}






//global state
store.subscribe(()=>{ // subscribe is used to listen to the changes in the store
                      // whenever the state changes, this function will be called
    history.push(store.getState());
   // console.log(history);
})








// Action creator is a function that returns an action object. It is used to create actions that can be dispatched to the store. Action creators are usually defined as functions that return an object with a type property and any additional data needed for the action.

/*
   async function init(){ // here we use async fuction So, it is return a promise
                               // but in redux we need to return a object
                               // so we use thunk middleware to handle async actions
                               // thunk middleware is used to handle async actions in redux
                               // it allows us to return a function instead of an action object
        const {data} = axios.get("http://localhost:3000/account/1");
        return {type:INIT, payload:data.amount}
   }

*/

 // redux-thunk middleware is provide to async fuction two orgument one is dispatch and second is getState
function getUserAccount(id){ // here we use async fuction So, it is return a promise
   return async(dispatch, getState) => {
       try{ 
            dispatch(getAccountUserPending())
            const {data} = await axios.get(`http://localhost:3000/account/${id}`);
            dispatch(getAccountUserFulFilled(data.amount));
       } catch (error) {
            dispatch(getAccountUserRejected(error.message));
       }
   } 
}
function getAccountUserFulFilled(value){
   return {type:GET_ACC_USER_FULFILLED, payload:value}
}
function getAccountUserRejected(error){
    return {type:GET_ACC_USER_REJECTED, error:error}
}
function getAccountUserPending(){
    return {type:GET_ACC_USER_PENDING}
}
function increment(){
    return {type:INCREMENT}
}
function decrement(){
    return {type:DECREMENT}
}
function incrementByAmount(value){
    return {type:INCREMENT_BY_AMOUNT, payload:value}
}
function incrementBonus(){
    return {type:INCREMENT_BONUS}
}






setTimeout(()=>{
   // store.dispatch({type:"increment"});
   // store.dispatch({type:"decrement"});

    // store.dispatch(init());
     console.log(store.dispatch(getUserAccount(3)))            // when use thunk middleware then in dispatch function we send function difinition
                                                          // Here store dispatch method change behaviour mean it get plan object then it is behave as redux but it get a function diffinition then it understand that function diffinition execute with these value (dispatch, getState)

    //console.log(store.dispatch(incrementByAmount(200)))
    //console.log(store.dispatch(incrementBonus()));
},2000)







 // redux have major three principles :- 
 // 1. redux have a global state
 // 2. can't mutate the state directly
 // 3. redux is a pure function, meaning it does not modify the original state but creates a new one based on the action received.





  return (
    <div>Redux</div>
  )
}

export default Redux 



