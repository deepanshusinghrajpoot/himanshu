import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'




export const adminApi = createApi({
    reducerPath: 'admin',
    baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:3000' }),
    endpoints: (build) => ({
      getAccounts: build.query({   // get is a query
        query: () => `/account`,
        providesTags: ['accounts'],  // providesTags in RTK Query is used for cache management — specifically, it tells RTK Query what kind of data a query provides, so that mutations can later invalidate that data if needed. 
                                     // providesTags helps RTK Query know what to refresh or refetch after a change happens in the backend.
      }),
      addAccount: build.mutation({   // POST method is a mutation
        query: ({userId, amount}) => ({
            url: '/account',
            method: 'POST',
            body: {amount, userId},
        }),
        invalidatesTags:['accounts']  // invalidatesTags tells RTK Query which cached data should be considered stale after a mutation — so it can automatically refetch the affected queries.
      }),
      deleteAccount: build.mutation({   // POST method is a mutation
        query: ({userId}) => ({
            url: `/account/${userId}`,
            method: 'DELETE',
        }),
        invalidatesTags:['accounts']  // invalidatesTags tells RTK Query which cached data should be considered stale after a mutation — so it can automatically refetch the affected queries.
      }),
      updateAccount: build.mutation({   // POST method is a mutation
        query: ({userId, amount}) => ({
            url: `/account/${userId}`,
            method: 'PATCH',
            body:{amount}
        }),
        invalidatesTags:['accounts']  // invalidatesTags tells RTK Query which cached data should be considered stale after a mutation — so it can automatically refetch the affected queries.
      }),
    }),
  })
  
  // Export hooks for usage in functional components, which are
  // auto-generated based on the defined endpoints
  export const { 
             useGetAccountsQuery, 
             useAddAccountMutation,
             useDeleteAccountMutation,
             useUpdateAccountMutation
         } = adminApi