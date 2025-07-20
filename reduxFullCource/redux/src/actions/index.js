import axios from "axios";



// action name constants
// const INIT = "account/init";
export const INCREMENT = "account/increment";
export const DECREMENT = "account/decrement";
export const INCREMENT_BY_AMOUNT = "account/incrementByAmount";
export const GET_ACC_USER_PENDING = "account/getUser/pending";
export const GET_ACC_USER_FULFILLED = "account/getUser/fulfilled";
export const GET_ACC_USER_REJECTED = "account/getUser/rejected";



export const INCREMENT_BONUS = "bonus/increment";



// redux-thunk middleware is provide to async fuction two orgument one is dispatch and second is getState
export function getUserAccount(id){ // here we use async fuction So, it is return a promise
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
 export function getAccountUserFulFilled(value){
    return {type:GET_ACC_USER_FULFILLED, payload:value}
 }
 export function getAccountUserRejected(error){
     return {type:GET_ACC_USER_REJECTED, error:error}
 }
 export function getAccountUserPending(){
     return {type:GET_ACC_USER_PENDING}
 }
 export function increment(){
     return {type:INCREMENT}
 }
 export function decrement(){
     return {type:DECREMENT}
 }
 export function incrementByAmount(value){
     return {type:INCREMENT_BY_AMOUNT, payload:value}
 }
 export function incrementBonus(){
     return {type:INCREMENT_BONUS}
 }
 