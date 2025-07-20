import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import axios from 'axios'

const initialState = {
  amount: 10,
}







// First, create the thunk
export const getUserAccount = createAsyncThunk(
    'account/getUser',
    async (userId, thunkAPI) => {
      try {
        const {data} = await axios.get(`http://localhost:3000/account/${userId}`)
        return data.amount
      } catch (error) {
        return error.message;
      }
    },
)









// Here all logic is modify of the complexity of redux :- If you want to see complexity then go to redux folder then inside action folder and see index.js file
// you see inside redux dev tool :- inspector
// where action is made:-  account/increment  

export const accountSlice = createSlice({
  name: 'account',
  initialState,
  reducers: {         
    increment: (state) => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the Immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes
      state.amount += 1
    },
    decrement: (state) => {
      state.amount -= 1
    },
    incrementByAmount: (state, action) => {
      state.amount += action.payload
    },
  },
  extraReducers: (builder)=>{
    builder.addCase(getUserAccount.fulfilled, (state, action)=>{
         state.amount = action.payload;
         state.pending = false;
    })
    .addCase(getUserAccount.pending, (state, action)=>{
        state.pending = true;
    })
    .addCase(getUserAccount.rejected, (state, action)=>{
        state.error = action.error;
    })
  }

})

// Action creators are generated for each case reducer function
export const { increment, decrement, incrementByAmount } = accountSlice.actions

export default accountSlice.reducer