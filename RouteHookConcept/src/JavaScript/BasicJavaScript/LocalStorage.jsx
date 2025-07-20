import React from 'react'


/*




✅ Web Storage API in JavaScript

✅ Comparison Table
Feature	                LocalStorage	      SessionStorage	     Cookies	     IndexedDB	       Cache Storage
Size Limit          	~5MB	              ~5MB	                 ~4KB	         Hundreds of MB    Large
Expiration	            Never	              On tab close	         Manual	         Manual	           Manual
Server Accessible	    ❌	                ❌	                  ✅	            ❌	             ❌
Async	                ❌	                ❌	                  ❌	            ✅	             ✅
Structured Data	        ❌	                ❌	                  ❌	            ✅	             ❌






✅ Common Methods

// Set Item
localStorage.setItem("key", "value");

// Get Item
localStorage.getItem("key");  // returns value or null

// Remove Item
localStorage.removeItem("key");

// Clear all data for current origin
localStorage.clear();









✅ Storing Objects in localStorage
localStorage only stores strings, so use JSON.stringify() and JSON.parse() for objects:


const user = { name: "Deepanshu Singh", city: "Gorakhpur" };

// Store object as string
localStorage.setItem("user", JSON.stringify(user));

// Retrieve and parse back to object
const userData = JSON.parse(localStorage.getItem("user"));

console.log(userData); // { name: "Deepanshu Singh", city: "Gorakhpur" }




✅ Reusable Utility Functions

// Store data in localStorage (handles objects)

function setData(key, value) {
    if (typeof value === "object") {
        localStorage.setItem(key, JSON.stringify(value));
    } else {
        localStorage.setItem(key, value);
    }
}



// Get data from localStorage (parses JSON if applicable)


function getData(key) {
    const data = localStorage.getItem(key);
    try {
        return JSON.parse(data);  // If valid JSON, parse
    } catch {
        return data;              // Otherwise, return raw string
    }
}




// Usage Example
setData("user", { name: "Deepanshu", role: "Developer" });
console.log(getData("user"));  // { name: "Deepanshu", role: "Developer" }
setData("token", "abc123");
console.log(getData("token"));  // "abc123"




✅ Quick One-Liner for Interviews
"Web Storage API allows persistent or session-based client-side storage using localStorage and sessionStorage, ideal for storing non-sensitive data as key-value pairs."






 */







const LocalStorage = () => {
  return (
    <div><h1>Local Storage</h1></div>
  )
}

export default LocalStorage