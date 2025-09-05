import React from 'react'


/*


⚛️ Client-Side Rendering (CSR) in React
----------------------------------------


🔹 What is Client-Side Rendering?
----------------------------------

In CSR, the server only sends a minimal index.html file and JavaScript bundles.

The browser runs JavaScript to generate and populate the DOM.

Since JavaScript is building the DOM, event listeners and interactivity 
are added automatically → No need for hydration.



🔹 Diagram (CSR Flow)
----------------------

   Server                                Client (Browser)
--------------------------------------------------------------
Sends: index.html  --->   Browser receives empty <div id="root">
                          + JavaScript bundle

                          JavaScript executes:
                          - Populates DOM
                          - Adds event listeners
                          - Runs React hooks (useState, useEffect, etc.)



🔹 Why Hydration is NOT Needed in CSR?
---------------------------------------

In CSR, JavaScript is responsible for both rendering the DOM and adding interactivity.
The page does not exist until JS executes, so there’s no pre-rendered HTML that needs to be hydrated.



🔹 Example (React App – CRA / Vite)
------------------------------------

Case 1: CSR (React.js App)

When JavaScript runs → DOM is populated and interactive.
If JavaScript is disabled → Page won’t render (you may see a blank screen or error).
That’s because JS is mandatory to create DOM.



Case 2: SSR (Next.js App)

HTML is already sent from the server.
Even if JS is disabled → You still see static content (but without interactivity).
Hydration is then needed to make it interactive.







🔹 Key Differences (CSR vs SSR + Hydration)
--------------------------------------------

| Feature            | CSR (React.js App)            | SSR + Hydration (Next.js)  |
| ------------------ | ----------------------------- | -------------------------- |
| Who builds DOM?    | Client-side JavaScript        | Server (HTML string)       |
| Initial load speed | Slower (JS must run first)    | Faster (HTML ready)        |
| SEO                | Poor (search bots see little) | Better (content available) |
| Hydration needed?  | ❌ No                         | ✅ Yes                    |
| If JS disabled     | ❌ Blank/error                | ✅ Static page (but dead) |



👉 In short:

CSR: Browser builds everything → Needs JS → No hydration.
SSR: Server builds HTML → Browser hydrates → Needs hydration for interactivity.



*/











const CSR = () => {
  return (
    <div>CSR</div>
  )
}

export default CSR