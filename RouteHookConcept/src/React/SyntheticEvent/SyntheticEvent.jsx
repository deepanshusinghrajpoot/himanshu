import React from 'react'

/*

✅ What is a Synthetic Event in React?
✔ Synthetic Event is a wrapper around the native browser event system, provided by React.
✔ It normalizes events across different browsers to ensure they behave consistently, avoiding browser-specific bugs.

✔ lll Synthetic events wrap around the native events and provide the same interface, making event handling predictable and consistent.


✅ Difference: Native DOM Events vs. React Synthetic Events
Native JavaScript Events	           React Synthetic Events
onclick	                               onClick
onchange	                           onChange
onmouseover	                           onMouseOver
onmouseenter	                       onMouseEnter

✔ Native events are lowercase, React events use camelCase.

✔ React Synthetic Events work the same way for all browsers, ensuring compatibility.

✅ Example of Synthetic Event in React

import React from 'react';

function App() {
    function handleClick(e) {
        console.log("Button Clicked");
        console.log(e);  // Synthetic Event object
    }

    return (
        <div>
            <button onClick={handleClick}>Click Me</button>
        </div>
    );
}

export default App;
✔ Here, onClick uses a Synthetic Event, but behaves similar to native click event.
✔ The e object is React's Synthetic Event, with properties similar to native events like target, type, etc.

✅ Extra Important Point for Interviews
✔ React Synthetic Events are part of the Event Delegation system, 
  meaning:
        Events are attached to the root of the DOM (document), not directly to individual elements.
        Improves performance by reducing the number of event listeners.



✅ Final Interview-Ready Statement
"In React, Synthetic Events are a cross-browser wrapper around native events. 
They provide a consistent interface for handling events like onClick, onChange, etc., regardless of the browser. 
Under the hood, React uses event delegation to attach these synthetic events efficiently."


*/


const SyntheticEvent = () => {
    function handleClick(e, value) {
        console.log("Button Clicked");
        console.log(e);  // Synthetic Event object
        alert(value);
    }

    return (
        <div> 
            <h1>Synthetic Event</h1>
            <button onClick={(e)=> handleClick(e, "Deepanshu are You learn Synthetic event")}>Click Me</button>
        </div>
    );
}

export default SyntheticEvent