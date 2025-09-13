/*

✅ React Components Overview

lll Components are the building blocks of any React App.

They help you split the UI into independent, reusable pieces and think about each piece in isolation.
Components are JavaScript functions (or classes) that:
Accept props (inputs)
Return React elements (UI)




✅ Capitalization Rule
Capitalized names (e.g., <App />) → Treated as components.
Lowercase names (e.g., <div />) → Treated as HTML tags.




✅ Types of Components

lll 1️⃣ Functional Components
Simple JavaScript functions is called functional component.
it Accept props and return React elements.

Easier to write and understand.

Example:

function Student(props) {
   return <h1>Hello {props.name}</h1>;
}
// OR
const Student = (props) => <h1>Hello {props.name}</h1>;


lll 2️⃣ Class Components

when ES6 classes extending React.Component is called class component.
In class component render() method is required.
Use this.props to access props.

Example:

class Student extends React.Component {
  render() {
    return <h1>Hello {this.props.name}</h1>;
  }
}

✅ Functional vs Class Component (Quick Summary)
Functional Component	                                    Class Component
Plain JavaScript function	                               ES6 Class extending React.Component
Accepts props as argument	                               Accesses props via this.props
Cannot use state directly (before React 16.8)	           Can use state and lifecycle methods
After React 16.8, can use useState, useEffect, etc.	      Has full access to lifecycle hooks

More concise, easier to test	Verbose syntax, older pattern




✅ Modern React Recommendation:
Prefer Functional Components with Hooks (useState, useEffect, etc.) because they simplify code and are the future direction of React.



*/