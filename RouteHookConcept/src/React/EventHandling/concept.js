/*
 
==================================== Event Handling ==============================================================
Handling events React element is very similar to handling events on DOM elements. There are some syntactic difference:

. React event are named using camelCase, rather than lowercase.
. With JSX you pass a function as the event handler, rather than string.


In HTML

<button onClick="handleClick()" >Click Me</button>

In React 

<button onClick={handleClick} >Click Me</button>   // Functional component
<button onClick={this.handleClick}>Click Me</button>  // Class Component 







You cannot return false to prevent default behavior in React. You must call preventDefault() explicitly.

In HTML
<a href="#" onClick="console.log("Clicked"); return false>Click Me</a>

In React
function handleClick(e){
  e.preventDefault();
  console.log("Clicked");
}









*/