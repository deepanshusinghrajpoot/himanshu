import React, { useState } from 'react'
import {useSelector, useDispatch} from "react-redux"
import {  incrementAmount, decrementAmount, decrementByAmount, incrementByAmount, multiplyByAmount } from '../redux/reducers/accountSlice';



const Amount = () => {
    

    const  dispatch = useDispatch();

    const {incrementOne, decrementOne, incrementByValue, decrementByValue, multiplyByValue,} = useSelector((state)=> state.account);

    const [value, setValue] = useState();


    return (
        <div>
            <h1>This is the Amount page</h1>

            <input type='number' placeholder='Enter a number...'  value={value}  onChange={(e)=> setValue(+e.target.value)} />

            <div>Amount:{incrementOne} <button onClick={()=>dispatch(incrementAmount())} >Increment amount by one</button></div>
            <div>Amount:{decrementOne} <button onClick={()=>dispatch(decrementAmount())} >Decrement by one</button></div>
            <div>Amount:{incrementByValue} <button onClick={()=> dispatch(incrementByAmount(value))} >Icrement the amount by a specific value</button></div>
            <div>Amount:{decrementByValue} <button onClick={()=> dispatch(decrementByAmount(value))} >Decrement the amount by a specific value</button> </div>
            <div>Amount:{multiplyByValue} <button onClick={()=> dispatch(multiplyByAmount(value))} >Maltiply the amount by a specific value</button> </div>
        </div>
    )
}



export default Amount