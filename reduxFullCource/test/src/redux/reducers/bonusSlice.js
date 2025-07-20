import { createSlice } from "@reduxjs/toolkit"


const initialState = {

    bonus:0,

}




const bonusSlice = createSlice({

    name:"bonus",
    initialState,
    reducers:{
        
        incrementBonusByOne:(state, action)=>{
            state.bonus += 1;
        },
        decrementBonusByOne:(state, action)=>{
            state.bonus -= 1;
        },
    
    }

})


export default bonusSlice

export const {
                  incrementBonusByOne,
                  decrementBonusByOne
                                              } = bonusSlice.actions