import { createSlice } from '@reduxjs/toolkit'






const initialState = {

    incrementOne:0,
    decrementOne:0,
    incrementByValue:0,
    decrementByValue:0,
    multiplyByValue:1,

    
}


const accountSlice = createSlice({

    name:"account",
    initialState,
    reducers:{
        incrementAmount:(state, action)=>{
            state.incrementOne  += 1;
        },
        decrementAmount:(state, action)=>{
            state.decrementOne  -= 1;
        },
        incrementByAmount:(state, action)=>{
            state.incrementByValue += action.payload;
        },
        decrementByAmount:(state, action)=>{
            state.decrementByValue -= action.payload;
        },
        multiplyByAmount:(state, action)=>{
            state.multiplyByValue  *= action.payload;
        },
    

    }
})


export default accountSlice

export const {
                     incrementAmount,
                     decrementAmount,
                     incrementByAmount,
                     decrementByAmount,
                     multiplyByAmount,
            

                                            } = accountSlice.actions