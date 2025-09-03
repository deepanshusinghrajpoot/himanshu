import React from 'react'


/*



✅ Debouncing vs. Throttling — Performance Optimization
✔lll Both Debouncing and Throttling are techniques used to improve performance of the application by limiting the rate at which function execution, especially for high-frequency events like:

Search inputs
Scroll events

Window resizing
Button clicks


✅ Core Difference — Quick Table
    Aspect	            Debouncing	                                 Throttling
lll Purpose	            Fires function after pause	                 Fires function at regular intervals
    Example             Use Search bars, Auto-suggestions	           Scroll tracking, Button spamming control
    Behavior	          Waits for user to stop actions	             Allows periodic execution regardless of activity
    API Calls	          Fires only after delay without new events	   Fires at fixed intervals during continuous activity




✅ Example for Interviews
🔥 Debouncing - E-commerce Search Bar
✔ Suppose you're building a Flipkart-like search bar:

Without Debouncing:
Typing Samsung Note triggers API calls on every keystroke = Poor performance

With Debouncing:
API call happens only after user stops typing for, say, 500ms
Reduces unnecessary server load


✅ Throttling - Resize Screen Event Explanation for Interview

✔ The resize event fires continuously as the user resizes the browser window.
✔ If we run expensive operations (like layout recalculations, DOM updates, or API calls) on every tiny pixel change, it severely affects performance.

With Throttling:
✔ We limit the execution of the resize handler to, say, once every 200ms.
✔ Even if the user continuously resizes the screen, the function executes at fixed intervals only.
✔ This ensures optimized performance, smoother UI, and prevents blocking the browser’s main thread.



✅ Key Interview Question
Which is better: Debouncing or Throttling?

✔ It depends entirely on the use case:

Use Case	                         Recommended Technique
Search Input	                     Debouncing
Auto-Suggestions	                 Debouncing
Scroll Performance	               Throttling
Button Click Limiting	             Throttling


*/










const ThrottlingVsDebouncing = () => {
  return (
    <div><h1>ThrottlingVsDebouncing</h1></div>
  )
}

export default ThrottlingVsDebouncing