import React from 'react'


/*

✅ React Capturing Phase Example
In React, to listen in the capturing phase, use event names with Capture:


export default function CapturingExample() {
    const grandParentClick = () => {
        console.log("Grandparent Capturing");
    };

    const parentClick = () => {
        console.log("Parent Capturing");
    };

    const childClick = () => {
        console.log("Child Clicked (Bubbling Phase)");
    };

    return (
        <div onClickCapture={grandParentClick} style={{ border: "2px solid black", padding: "20px" }}>
            Grandparent
            <div onClickCapture={parentClick} style={{ border: "2px solid blue", padding: "20px" }}>
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
    Grandparent Capturing
    Parent Capturing
    Child Clicked (Bubbling Phase)

✔ Capturing handlers (onClickCapture) run top-down, then normal bubbling happens.



*/


const Capturing = () => {
  
    
    const grandParentClick = () => {
        console.log("Grandparent Capturing");
    };

    const parentClick = () => {
        console.log("Parent Capturing");
    };

    const childClick = () => {
        console.log("Child Clicked (Bubbling Phase)");
    };

    return (
        <div onClickCapture={grandParentClick} style={{ border: "2px solid black", padding: "20px" }}>
            Grandparent
            <div onClickCapture={parentClick} style={{ border: "2px solid blue", padding: "20px" }}>
                Parent
                <div onClick={childClick} style={{ border: "2px solid red", padding: "20px" }}>
                    Child
                </div>
            </div>
        </div>
    );


}

export default Capturing