import { createAction, createReducer } from '@reduxjs/toolkit'






export const increment = createAction('reward/increment');  // this action is automatically create by slice method
export const incrementByAmount = createAction('reward/incrementByAmount');  // this action is automatically create by slice method



const initialState = {
    rewards: 15,
}


const rewardReducer = createReducer(initialState, (builder) => {
    builder
      .addCase(increment, (state, action) => {
        state.rewards++
      })
      .addCase(incrementByAmount, (state, action) => {
        state.rewards += action.payload
      })

})



export default rewardReducer
