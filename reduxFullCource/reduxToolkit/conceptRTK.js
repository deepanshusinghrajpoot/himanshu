

/*

========================================= Redux Toolkit ==============================================

RTK Query is a powerful data fetching and caching tool. It is designed to simplify common cases for loading data in a web application, eliminating the need to hand-write data fetching & caching logic yourself.

RTK Query is an optional addon included in the Redux Toolkit package, and its functionality is built on top of the other APIs in Redux Toolkit.




The data fetching and caching logic is built on top of Redux Toolkit's createSlice and createAsyncThunk APIs

RTK Query can also generate React hooks that encapsulate the entire data fetching process, provide data and isLoading fields to components, and manage the lifetime of cached data as components mount and unmount

Finally, RTK Query is completely written in TypeScript, and is designed to provide an excellent TS usage experience





What's included


   React-specific entry point that automatically generates
   hooks corresponding to the defined endpoints 

   import { createApi } from '@reduxjs/toolkit/query/react'






createApi(): The core of RTK Query's functionality. It allows you to define a set of "endpoints" that describe how to retrieve data from backend APIs and other async sources, including the configuration of how to fetch and transform that data. In most cases, you should use this once per app, with "one API slice per base URL" as a rule of thumb.
fetchBaseQuery(): A small wrapper around fetch that aims to simplify requests. Intended as the recommended baseQuery to be used in createApi for the majority of users.
<ApiProvider />: Can be used as a Provider if you do not already have a Redux store.
setupListeners(): A utility used to enable refetchOnMount and refetchOnReconnect behaviors.





*/