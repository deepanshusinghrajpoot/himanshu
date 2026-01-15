/*


  ============================== Mounting Phase ======================================

  Mounting- Mounting is the process of creating an element and inserting it in a DOM tree.
         
  When an instance of a React component is created and inserted into the DOM, the following methods are called in order:"

  There are foure methods exist in mounting phase
  -----------------------------------------------
          1. constructor() — It initializes state and binds methods.
          2. static getDerivedStateFromProps() — Rarely used; updates state based on props before rendering.
          3. render() — Returns JSX to build the UI.
          4. componentDidMount() — Runs once after the component mounts; used for API calls, DOM updates, or side effects.

  ----------------------- 1. constructor() ----------------------------------
  
  lll The constructor for a React component is called before it is mounted.
   
  When implementing the constructor for a React.Component subclass, 
  you/we should call super(props) before any other statement. Otherwise, this.props will be undefined in the constructor, which can lead to bugs.

  React constructor are only used for two purposes:
      .  Initializing local state — by assigning an object to this.state.
         Example: this.state = { name: "Rahul" }

      .  Binding event handler methods to the component instance — to ensure correct this context.
         Example: this.handleClick = this.handleClick.bind(this)

  ----------------------- 2. static getDerivedStateFromProps() ----------------------------------

       learn 1 :- getDerivedStateFromProps is invoked right before calling the render method, 
                  both on the initial mount and on subsequent update.
                 
       learn 2 :- It should return an object to update the state, or null to update nothing.
                  This method exists for rare use cases where the state depends on changes in props over time.
                  This method doesn't have access to the component instance. As it is static method so this keyWord is not available inside this method.



  syntax:- static getDerivedStateFromProps(props, state){}



  ----------------------- 3. render() ----------------------------------

✅ React render() Method - Perfect Interview Notes
✔ The render() method is the only required method in a React class component.
✔ It examines this.props and this.state.


✅ render() Can Return:
Type	                                    Description
React Elements	                            Created via JSX or React.createElement. E.g., <div>, <MyComponent>
Array or Fragments	                        Allows returning multiple elements without extra DOM nodes.
Portals	                                    Render children into a different part of the DOM tree.
Boolean or null	                            Renders nothing to the DOM. Useful for conditional rendering.


✅ Important Note for Interviews
✔ The render() method should be pure, meaning:
      It does not modify component state directly
      It produces the same output every time it's called with the same state/props
      It does not interact directly with the DOM (e.g., no document.querySelector inside render())


✅ Quick Example
class Demo extends React.Component {
    render() {
        return (
            <div>
                <h1>Hello {this.props.name}</h1>
            </div>
        );
    }
}
✔ The method uses this.props.name to decide what to render.


✅ Final Interview Statement
"In a class component, render() is the only required method. It returns React elements, arrays, portals, or null based on the current props and state.
The function must be pure — it should not modify state or interact with the browser directly."        



  
  ----------------------- 4. componentDidMount() ----------------------------------

✅ componentDidMount() - Interview-Ready Notes

✔ componentDidMount() is a lifecycle method in React Class Components.
✔ It is invoked immediately after the component is mounted into the DOM, i.e., after the first render.
✔ It runs only once per component lifecycle.


✅ When to Use componentDidMount()

Ideal place for:
       API calls or fetching data
       Adding event listeners
       Working with DOM nodes
       Starting timers or animations


✅ Code Example

class Demo extends React.Component {
    componentDidMount() {
        console.log("Component Mounted");
        // Example: API Call
        fetch('https://api.example.com/data')
            .then(res => res.json())
            .then(data => console.log(data));
    }

    render() {
        return <h1>Hello World</h1>;
    }
}
✔ componentDidMount() is triggered after the first render, perfect for side-effects like data fetching.


✅ Important Notes for Interviews
       Runs only once, after initial render
       Safe to interact with the DOM here
       Avoid calling setState() inside it in a loop — may cause infinite re-renders

lll      Equivalent to useEffect(() => { }, []) in functional components

lll ✅ Final Interview Statement
    "componentDidMount() runs once after the component mounts. It's ideal for side-effects like API calls, DOM manipulations, or setting up subscriptions. 
     It ensures the component is rendered before performing operations."



*/










































