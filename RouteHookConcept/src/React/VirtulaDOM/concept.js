/*


DOM (Document Object Model):- It is a tree like structur of HTML page (eg:- HTML(two child Header and body))



            O                            O                             O
          .   .                        .   .                         .   . 
        O      O changes              O     O update                O     O re-rendering
      .  .     .                    .  .    .                      . .    .
     O   O     O                   O    O   O update              O   O   O re-rendering

    state changes    ---------->  Compute diffing --------------> re-rendering 


🧠 Virtual DOM vs. Real DOM

Virtual DOM (VDOM): This is a lightweight, in-memory representation of the real DOM.
It contains essential properties like type, props, and children, making it faster to create and compare.​

Real DOM: This is the actual Document Object Model rendered in the browser.
It's more complex and includes numerous properties and methods, making direct manipulation more resource-intensive.


lll 🧠 Understanding the Virtual DOM

The Virtual DOM is like a lightweight blueprint of the actual web page.
Instead of updating the real page directly every time something changes, React first updates this blueprint.
This approach allows React to determine the most efficient way to apply changes, enhancing performance.​


🔄 The Diffing Algorithm

When changes occur, React compares the new Virtual DOM with the previous version using a process called diffing.
This comparison identifies exactly what has changed.
React then updates only those specific parts in the real DOM, rather than re-rendering the entire page.
This selective updating approach ensures faster and more efficient performance.​


🔄 Reconciliation: Applying the Changes

After identifying the differences through diffing, React proceeds to the reconciliation phase. 
Here, it updates only the parts of the actual DOM that have changed, rather than re-rendering the entire page.
This selective updating approach ensures faster and more efficient performance.​



🧵 What Is React Fiber?

React Fiber is the reimplementation of React's core reconciliation algorithm introduced in React 16.
It enhances the reconciliation process by enabling incremental rendering,
prioritizing updates, and improving responsiveness. Fiber breaks down rendering work into units that can be paused,
resumed, or aborted, allowing React to handle complex updates more efficiently.






🌳 DOM (Document Object Model)
The DOM is a tree-like structure representing the HTML content of a webpage.

Example:

<html>
  <head></head>
  <body>
    <h1>Hello</h1>
    <p>World</p>
  </body>
</html>

This would look like:

          html
         /    \
      head    body
                |
              [h1, p]




✅ In Interview, If Asked:
lll Q: What is Virtual DOM? Why does React use it?

The Virtual DOM is like a lightweight blueprint of the actual web page.
Instead of updating the real page directly every time something changes, React first updates this blueprint.
This approach allows React to determine the most efficient way to apply changes, enhancing performance.​





⚛️ Virtual DOM vs Real DOM
Feature	                               Virtual DOM	                               DOM
Type	                                 Lightweight JavaScript object	             Actual browser DOM
Speed	                                 Fast – changes computed in memory	         Slower – direct manipulation
Usage	                                 Used in React for efficient updates	       Used by browser for rendering
Updates	                               Via diffing + patching	                     Re-render entire tree/element





⚙️ React Rendering Lifecycle

State/Props Change
       ↓
Create New Virtual DOM
       ↓
Diffing (compare with old VDOM)
       ↓
Reconciliation (update only changed parts in Real DOM)
       ↓
Browser Paints UI

✅ React avoids unnecessary DOM manipulations by comparing the Virtual DOMs.


lll 🔍 Diffing Algorithm
     When something changes (state/props) of component, 
     React: Creates a new Virtual DOM.
     Compares it with the old one (using diffing algorithum).
     And Finds minimal changes.
     Updates only changed nodes in the Real DOM.


lll 🔁 Reconciliation
    After identifying the differences through diffing, React proceeds to the reconciliation phase. 
    Here, it updates only the parts of the actual DOM that have changed, rather than re-rendering the entire page.
    ​




🧵 React Fiber (introduced in React 16)

React Fiber is the new reconciliation engine that:

Allows React to split rendering work into small units (called "fibers").

Makes rendering interruptible (i.e., pause/resume).

Enables prioritization of updates:

e.g., animations get higher priority than logging in background.

✅ This makes React more responsive and suitable for modern UI patterns.









lll Q: What is React Fiber?

React Fiber is the reimplementation of React's core reconciliation algorithm introduced in React 16.
It enhances the reconciliation process by enabling incremental rendering, prioritizing updates, and 
improving responsiveness. 

Fiber breaks down rendering work into units that can be paused,
resumed, or aborted, allowing React to handle complex updates more efficiently.









✅ Add These Key Points After Your Paragraph:


🔄 1. Dual Fiber Trees (Current vs Work-in-Progress)
React maintains two copies of the Fiber tree:

    Current Tree – The one currently shown on the screen (UI).
    Work-in-Progress Tree – The one being built in memory when updates happen.

Once the update is complete, the WIP tree is committed and becomes the current tree.







🧵 2. Fiber as a Linked List Tree Structure

   Each Fiber node is connected to:
   child → first child
   sibling → next sibling
   return → parent node
   This makes traversal efficient using a linked list structure instead of a plain tree.








🧠 3. Two Phases of Reconciliation

🔹 Render Phase (Can be paused)
         Builds the Work-in-Progress tree.
         xecutes in chunks.
         Prepares a list of changes (called the “effect list”).

🔸 Commit Phase (Cannot be paused)
         Applies the calculated changes to the real DOM.
         Runs synchronously.
         Triggers lifecycle methods like componentDidMount, useEffect.







🧪 4. Fiber Enables Features Like:
      Concurrent Mode (via startTransition, useDeferredValue)
      Suspense for Data Fetching
      Time-slicing for responsiveness
      Error boundaries













*/