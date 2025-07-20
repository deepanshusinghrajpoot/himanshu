import React from 'react'
import UseMemoExample1 from './UseMemoExample1'

const UseMemo = () => {
  /*
     =================== useMemo ===================

     The React useMemo Hook return a memoized value.(it's like caching a value that It doesn't need to be recalculated.)

     The useMemo Hook only runs when one of its dependencies gets updated

     This can improve the performance of the application. There is one more hook in react to improve performance,
     that is useCallback hook.

     The useMemo and useCallback Hooks are similar. the main difference is:
     - useMemo return a memoized value.
     - useCallback return a memoized function
  */


  return (
    <div>
         <h1>=================== useMemo Hook example ===================</h1>
         <h3>------- Example 1 ---------</h3> 
         <UseMemoExample1 />
    </div>
  )
}

export default UseMemo