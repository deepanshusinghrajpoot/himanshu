import React from 'react'
import {useEffect} from 'react'


/*

✅ Throttling Example: Window Resize Event

// Throttle Function Definition
const throttle = (fn, limit) => {
    let flag = true;
    return function (...args) {
        const context = this;
        if (flag) {
            fn.apply(context, args);
            flag = false;
            setTimeout(() => {
                flag = true;
            }, limit);
        }
    };
};

// "We store this to ensure the throttled function maintains the correct reference to the event target,
//  preserving context across delayed or wrapped function calls."



// Expensive Function Example
const expensive = () => {
    console.log("Expensive Function Triggered", new Date().toLocaleTimeString());
};



// Creating a Throttled Version
const betterExpensive = throttle(expensive, 2000);  // Allow once every 2 seconds



// Event Listener Using Throttling
window.addEventListener("resize", betterExpensive);









✅ Explanation for Interviews
✔ Without throttling, the resize event fires continuously, leading to performance issues.
✔ With throttling, expensive() runs at most once every 2 seconds, no matter how often the event triggers.
✔ Ensures efficient, controlled execution of costly operations like DOM updates or API calls.




✅ Common Interview Add-On
Can we throttle scroll events, button clicks, etc.?
✔ Yes, throttling applies to any high-frequency event where limiting execution is necessary.





*/




const Throttling = () => {


  // Expensive Function to run on resize
    const handleResize = () => {
        console.log("Resized at", new Date().toLocaleTimeString());
    };

    // Throttle Function Definition
    const throttle = (fn, limit) => {
        let flag = true;
        return function (...args) {
            const context = this;
            if (flag) {
                fn.apply(context, args);
                flag = false;
                setTimeout(() => {
                    flag = true;
                }, limit);
            }
        };
    };


    useEffect(() => {
        const throttledResize = throttle(handleResize, 5000);

        window.addEventListener("resize", throttledResize);

        // Cleanup to avoid memory leaks
        return () => {
            window.removeEventListener("resize", throttledResize);
        };
    }, []);

    return (
        <div style={{ padding: "20px" }}>
            <h2>React Throttling Example</h2>
            <p>Resize the window and check the console. Function runs every 2 seconds at max.</p>
        </div>
    );
}

export default Throttling