import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import { configureStore } from '@reduxjs/toolkit'
import accountReducer from './slices/accountSlices.js'
import bonusReducer  from './slices/bonusSlice.js'
import {Provider} from 'react-redux'
import rewardReducer from './reducers/reward.js'
import { adminApi } from './api/adminSlice.js'




const store = configureStore({
    reducer:{
       account: accountReducer,
       bonus: bonusReducer,
       reward: rewardReducer,
       [adminApi.reducerPath]: adminApi.reducer,    //  [adminApi.reducerPath] when we give key inside square bracket then get key value otherwise get string
    },
    
    // Adding the api middleware enables caching, invalidation, polling,
    // and other useful features of `rtk-query`.
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware().concat(adminApi.middleware),
})







createRoot(document.getElementById('root')).render(
  <StrictMode>
      <Provider store={store} >
          <App />
      </Provider>
  </StrictMode>,
)
