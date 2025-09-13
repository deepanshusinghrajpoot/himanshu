import React from 'react'


/*




⚛️ Hydration in React (Interview Notes)
----------------------------------------



lll🔹 What is Hydration?
-----------------------

In Server-Side Rendering (SSR), React generates an HTML string on the server using renderToString(component) and sends it to the client.

This HTML is static (no interactivity, no event listeners, no useEffect execution).

Hydration is the process where React takes this server-rendered HTML and attaches event listeners, states, and React-specific 
behavior on the client to make the page fully interactive.




🔹 Diagram (Flow of SSR + Hydration)
-------------------------------------


   Server (SSR)                           Client (Browser)
--------------------------------------------------------------
renderToString(component)  --->   Receives HTML, CSS, JS (string)
                                  (But NOT interactive yet)

                                  hydrate(component)
                        <---   React attaches state, event listeners,
                               effects → Page becomes interactive





🔹 Why Hydration is Needed?
-----------------------------

HTML received from server is just static markup.

Without hydration:
       Click events won’t work.
       useState, useEffect, and other hooks won’t run.
       UI is visible but dead/static.


With hydration:
       React "re-uses" the server HTML.
       Binds event listeners.
       Initializes state & lifecycle hooks.
       Page becomes dynamic & interactive.




🔹 Example (Next.js)
---------------------

Case 1: JavaScript disabled in browser
→ You see the HTML, but buttons/inputs do not work.
→ No hydration → No interactivity.

Case 2: JavaScript enabled
→ React hydrates the server HTML.
→ State, event listeners, hooks (useEffect, useState) work.
→ Page is fully interactive.



🔹 Key Points for Interviews
-----------------------------

Hydration = Attaching interactivity to server-rendered HTML.
SSR improves performance & SEO (faster first paint).
Hydration ensures React features (hooks, events) work on client side.
Next.js, Remix, and similar frameworks rely on hydration.



👉 So, in simple words:
SSR = Page loads faster (HTML ready).
Hydration = React makes that HTML alive (interactive).



 */









const SSR = () => {
  return (
    <div>SSR</div>
  )
}

export default SSR