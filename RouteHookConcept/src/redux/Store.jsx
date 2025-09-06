/*

🏪 Redux Store (RTK) – Main Parts


1. configureStore
-----------------

👉 “I use configureStore in RTK to set up the store. It simplifies configuration by combining reducers and applying middleware in one place.”





2. reducer
----------

reducer: {
   [x.name]: x.reducer
}


👉 “Reducers describe how state updates. In RTK, we combine multiple slice reducers inside the store’s reducer object.”




3. middleware
-------------

middleware: (defaultMiddleware) => [
  ...defaultMiddleware(),
  api.middleware
]


👉 “Middleware handles side effects like async API calls. RTK gives default middleware, and we can add extra ones like api.middleware.”




✅ Interview One-liner:

"In RTK, the store is created using configureStore, where we provide reducers for state management, middleware for side effects, and RTK automatically wires up DevTools support."














import { configureStore } from "@reduxjs/toolkit"
import authSlice from './reducers/auth'
import api from "./api/api"
import miscSlice from "./reducers/misc"
import chatSlice from "./reducers/chat"


const store = configureStore({

    reducer: {
       [authSlice.name]: authSlice.reducer, 
       [miscSlice.name]: miscSlice.reducer,
       [chatSlice.name]: chatSlice.reducer,
       [api.reducerPath]: api.reducer,
    },
    middleware: (defaultMiddleware)=> [...defaultMiddleware(), api.middleware],
})



export default store







*/