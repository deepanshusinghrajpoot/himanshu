import { configureStore } from '@reduxjs/toolkit'
import miscSlice from './redux/reducers/msciSlice'
import accountSlice from './redux/reducers/accountSlice'
import bonusSlice from './redux/reducers/bonusSlice'




const store = configureStore({

    reducer:{

        [miscSlice.name]: miscSlice.reducer,
        [accountSlice.name]: accountSlice.reducer,
        [bonusSlice.name]: bonusSlice.reducer,

    }

})


export default store