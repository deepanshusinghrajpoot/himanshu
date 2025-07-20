import { DECREMENT, GET_ACC_USER_FULFILLED, GET_ACC_USER_PENDING, GET_ACC_USER_REJECTED, INCREMENT, INCREMENT_BY_AMOUNT } from '../actions/index'




// reducer is a function that takes the current state and an action as arguments and returns a new state. It is a pure function, meaning it does not modify the original state but creates a new one based on the action received.
export function accountReducer(state={amount:1}, action) {
    
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
