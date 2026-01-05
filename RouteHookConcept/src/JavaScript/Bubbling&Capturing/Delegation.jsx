import React from 'react'



/*


✅ Event Delegation in JavaScript
✔lll  Event Delegation is a technique where you/we attach a single event listener to a parent element, and handle events for its current or future child elements using event bubbling.


✅ Why Event Delegation?
Attaching individual event listeners to every element increases:

Memory consumption
Performance issues (especially in dynamic UIs like infinite scroll or lazy-loading lists)


✔ With Event Delegation:
One listener handles all child events via bubbling phase
Saves memory, improves performance, simplifies code



✅ Practical Example: E-Commerce Categories

<ul id="category">
    <li id="laptop">Laptop</li>
    <li id="camera">Camera</li>
    <li id="shoes">Shoes</li>
</ul>

document.getElementById("category").addEventListener('click', (e) => {
    if (e.target.tagName === 'LI') {
        window.location.href = "/" + e.target.id;
    }
});


Explanation:
Listener is added to <ul id="category">
Clicks on <li> items bubble up
Handler checks e.target.tagName to ensure the click came from <li>
Redirects based on id



✅ Real-Time Form Example

<div id="form">
    <input type="text" id="name" data-uppercase>
    <input type="text" id="pan">
    <input type="text" id="mobile">
</div>

document.getElementById("form").addEventListener('keyup', (e) => {
    if (e.target.dataset.uppercase !== undefined) {
        e.target.value = e.target.value.toUpperCase();
    }
});


Notes:
   Only input with data-uppercase attribute converts text to uppercase
   Demonstrates selective handling using event delegation



✅ Advantages of Event Delegation
✔ Memory-efficient (fewer event listeners)
✔ Works for dynamically added elements
✔ Cleaner, maintainable code
✔ Essential for infinite scroll, lazy-loaded content



✅ Limitations
⚠ Not all events bubble (e.g., focus, blur)
⚠ Must avoid e.stopPropagation() for bubbling to work
⚠ Can get complex with deeply nested elements or mixed bubbling/capturing scenarios




✅ Interview Shortcut Answer
"Event Delegation leverages event bubbling by attaching a single listener to a parent, improving performance and handling child events, even for dynamically created elements."






*/





const Delegation = () => {
  return (
    <div><h1>Delegation</h1></div>
  )
}

export default Delegation