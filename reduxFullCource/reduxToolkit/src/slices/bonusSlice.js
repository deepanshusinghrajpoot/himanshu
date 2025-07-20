import { createAction, createSlice } from '@reduxjs/toolkit'




const incrementByAmount = createAction("account/incrementByAmount");



const initialState = {
  points: 11,
}

// Here all logic is modify of the complexity of redux :- If you want to see complexity then go to redux folder then inside action folder and see index.js file

export const bonusSlice = createSlice({
  name: 'bonus',
  initialState,
  reducers: {         
    increment: (state) => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the Immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes
      state.points += 1
    },
  },
  extraReducers: (builder)=>{   // 1. extar reducer use when we want to add specific action which is by default not made here 
                                // 2. async function is also add inside extra reducer
      builder.addCase(incrementByAmount,(state, action)=>{
          if(action.payload >= 100){
             state.points++
          }
      })
  }



})





// Action creators are generated for each case reducer function
export const { increment } = bonusSlice.actions

export default bonusSlice.reducer