import React from 'react'


/*


✅ Event Propagation in JavaScript
Three Phases of Event Propagation:

lll Capturing Phase (Trickling Down)
------------------------------------

In capturing pahse Event moves from the top (document) down to the target element.
Event Capturing triggered by setting useCapture = true in addEventListener.





Target Phase
Event reaches the target element — always fires at the element itself.





lll Bubbling Phase (Bottom-Up)
--------------------------

In Bubbling phase Event bubbles up from the target element to the top (document).
Event Bubbling is a Default phase of the addEventListener (useCapture = false).




✅ Example Setup

<style>
    div {
        min-width: 100px;
        min-height: 100px;
        padding: 30px;
        border: 1px solid black;
    }
</style>

<div id="grandparent">
    Grandparent
    <div id="parent">
        Parent
        <div id="child">
            Child
        </div>
    </div>
</div>



✅ Bubbling Example (Default Behavior)
---------------------------------------

document.querySelector("#grandparent").addEventListener('click', () => {
    console.log("Grandparent Clicked!");
});

document.querySelector("#parent").addEventListener('click', () => {
    console.log("Parent Clicked!");
});

document.querySelector("#child").addEventListener('click', () => {
    console.log("Child Clicked!");
});



✔ Click on Child Div

Output:
         Child Clicked!
         Parent Clicked!
         Grandparent Clicked!



✅ Capturing Example
---------------------

document.querySelector("#grandparent").addEventListener('click', () => {
    console.log("Grandparent Clicked!");
}, true);

document.querySelector("#parent").addEventListener('click', () => {
    console.log("Parent Clicked!");
}, true);

document.querySelector("#child").addEventListener('click', () => {
    console.log("Child Clicked!");
}, true);



✔ Click on Child Div

Output:
        Grandparent Clicked!
        Parent Clicked!
        Child Clicked!


✅ Mixed Example (Capturing + Bubbling)  first perform capturing then bubbling
-------------------------------------------------------------------------------

document.querySelector("#grandparent").addEventListener('click', () => {
    console.log("Grandparent Clicked!");
}, true);  // Capturing

document.querySelector("#parent").addEventListener('click', () => {
    console.log("Parent Clicked!");
});  // Bubbling

document.querySelector("#child").addEventListener('click', () => {
    console.log("Child Clicked!");
}, true);  // Capturing


✔ Click on Child Div

Output:
        Grandparent Clicked!
        Child Clicked!
        Parent Clicked!



✅ Stopping Propagation (Prevent Bubbling Up)

document.querySelector("#grandparent").addEventListener('click', () => {
    console.log("Grandparent Clicked!");
});

document.querySelector("#parent").addEventListener('click', (e) => {
    console.log("Parent Clicked!");
    e.stopPropagation();  // Stops further bubbling
});

document.querySelector("#child").addEventListener('click', () => {
    console.log("Child Clicked!");
});



✔ Click on Child Div


Output:
     Child Clicked!
     Parent Clicked!



✔ Click on Parent Div directly

Output:
     Parent Clicked!



✅ Interview One-Liner
"Event propagation has capturing (top-down) and bubbling (bottom-up) phases. We can control this using the third parameter of addEventListener. 
stopPropagation() halts further propagation to improve performance or control behavior.



-----------------------------------------------------------------------------------------------------------------------------------------------

✅ Event Bubbling & Capturing in React
✔ React uses a Synthetic Event System, which wraps native events for better cross-browser compatibility.

✔lll By default, all React events bubble up to the root, similar to plain JavaScript.
✔lll React supports capturing phase by adding Capture suffix to event handlers.


✅ React Event Bubbling Example

export default function BubblingExample() {

    const grandParentClick = () => {
        console.log("Grandparent Clicked");
    };

    const parentClick = () => {
        console.log("Parent Clicked");
    };

    const childClick = () => {
        console.log("Child Clicked");
    };

    return (
        <div onClick={grandParentClick} style={{ border: "2px solid black", padding: "20px" }}>
            Grandparent
            <div onClick={parentClick} style={{ border: "2px solid blue", padding: "20px" }}>
                Parent
                <div onClick={childClick} style={{ border: "2px solid red", padding: "20px" }}>
                    Child
                </div>
            </div>
        </div>
    );
}

✔ Click on Child Div

Output:
     Child Clicked
     Parent Clicked
     Grandparent Clicked
     
➡ Just like plain JS, events bubble upward by default.




*/







const Bubbling = () => {

    const grandParentClick = () => {
        console.log("Grandparent Clicked");
    };

    const parentClick = () => {
        console.log("Parent Clicked");
    };

    const childClick = () => {
        console.log("Child Clicked");
    };

    return (
        <div onClick={grandParentClick} style={{ border: "2px solid black", padding: "20px" }}>
            Grandparent
            <div onClick={parentClick} style={{ border: "2px solid blue", padding: "20px" }}>
                Parent
                <div onClick={childClick} style={{ border: "2px solid red", padding: "20px" }}>
                    Child
                </div>
            </div>
        </div>
    );
}





export default Bubbling