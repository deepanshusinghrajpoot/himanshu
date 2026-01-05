/*


====================================== Updating Phase ==========================================

Updating - Updating is the process of changing state or props of component and update changes to node already in the DOM.

"When a React component is re-rendered due to changes in state or props , these methods are called in order:"

There are five methods exist in updating phase. They are calling in followig order.
-----------------------------------------------------------------------------------
        1. static getDerivedStateFromProps()
        2. shouldComponentUpdate()
        3. render()      
        4. getSnapshotBeforeUpdate()
        5. componentDidUpdate()
 
   here render() and componentDidUpdate() very imp



  ----------------------- 2. static getDerivedStateFromProps() ----------------------------------

  getDerivedStateFromProps is invoked right before calling the render method, both on the initial mount and on subsequent update.
  It should return an object to update the state, or null to update nothing.
  This method exists for rare use cases where the state depends on changes in props over time.
  This method doesn't have access to the component instance.It is static methode so this keyword is not exist in this method.

  syntax:- 

  static getDerivedStateFromProps(props, state){}

  
  ----------------------- 2.  shouldComponentUpdate() ----------------------------------

 lll "shouldComponentUpdate() lets React decide whether to re-render the component or skip rendering, based on state or prop changes."

 ✔ It is called before re-rendering, when new state or props are received.

lll ✔ By default, it returns true, meaning React will re-render.
lll ✔ If it returns false, React skips the render() method to optimize performance.

  return shouldComponentUpdate(nextProps, nextState){}





  ----------------------- 3. render() ----------------------------------

✅ React render() Method - Perfect Interview Notes
✔ The render() method is the only required method in a React class component.
✔ It examines this.props and this.state.


✅ render() Can Return:
Type	                                     Description
React Elements	                            Created via JSX or React.createElement. E.g., <div>, <MyComponent>
Array or Fragments	                      Allows returning multiple elements without extra DOM nodes.
Portals	                                  Render children into a different part of the DOM tree.
Boolean or null	                         Renders nothing to the DOM. Useful for conditional rendering.


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


  

 ----------------------- 4. getSnapshotBeforeUpdate() ----------------------------------          

✅ getSnapshotBeforeUpdate() - Interview-Ready Notes

✔ getSnapshotBeforeUpdate() is a lifecycle method in React Class Components.

lll ✔ It is invoked right before the changes are committed to the actual DOM, i.e., after the render but before the DOM update.
    ✔ Useful for capturing information from the DOM before it gets updated, like scroll position or element measurements.

    

✅ Syntax

getSnapshotBeforeUpdate(prevProps, prevState) {
    // Capture information before DOM updates
    return snapshotValue;
}
✔ The value returned from getSnapshotBeforeUpdate() is passed as the third argument to componentDidUpdate().


✅ When to Use
Capture scroll positions
Save dimensions of elements
Compare previous vs updated DOM state
Prepare for animations based on current DOM layout



✅ Example
class Demo extends React.Component {
    listRef = React.createRef();

    getSnapshotBeforeUpdate(prevProps, prevState) {
        if (prevProps.messages.length < this.props.messages.length) {
            // Capture scroll position before update
            return this.listRef.current.scrollHeight;
        }
        return null;
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        if (snapshot !== null) {
            this.listRef.current.scrollTop +=
                this.listRef.current.scrollHeight - snapshot;
        }
    }

    render() {
        return (
            <div ref={this.listRef} style={{ overflowY: "scroll", height: "200px" }}>
                {this.props.messages.map((msg, index) => (
                    <p key={index}>{msg}</p>
                ))}
            </div>
        );
    }
}
✔ Before new messages are rendered, we capture the current scroll height
✔ After DOM updates, we adjust scroll position using the snapshot



lll ✅ Final Interview Summary
"getSnapshotBeforeUpdate() runs after render but before the DOM is updated. 
It's used to capture information like scroll position or measurements that might change after the update. 
The returned value is passed to componentDidUpdate() for use after DOM changes."




 ----------------------- 5. componentDidUpdate() ----------------------------------

✅ componentDidUpdate() - Interview-Ready Notes
✔ componentDidUpdate() is a React Class Component lifecycle method.
✔ It is invoked immediately after the component updates, i.e., after render() is called and the changes have been committed to the DOM.
✔ It does NOT run after the initial render, only on updates caused by state or props changes.

✅ Common Uses of componentDidUpdate()
✔ Re-initialize third-party libraries (e.g., charts, sliders) after DOM updates
✔ Compare previous props or state with current to conditionally run logic
✔ Handle manual DOM operations
✔ Trigger network calls based on specific state/prop changes

✅ Syntax

componentDidUpdate(prevProps, prevState, snapshot) {
    // Compare current and previous props/state
}
✔ If getSnapshotBeforeUpdate() is implemented, its return value is received as the snapshot parameter.
✔ If not, snapshot is undefined.

✅ Important Interview Notes
✔ componentDidUpdate() will not run if shouldComponentUpdate() returns false.
✔ Be cautious using setState() inside componentDidUpdate() — it can lead to infinite loops if not properly checked.

✅ Example

class Demo extends React.Component {
    componentDidUpdate(prevProps, prevState, snapshot) {
        if (prevProps.count !== this.props.count) {
            console.log("Count updated:", this.props.count);
        }

        if (snapshot !== null) {
            console.log("Snapshot from getSnapshotBeforeUpdate:", snapshot);
        }
    }

    render() {
        return <h1>{this.props.count}</h1>;
    }
}
✔ Only runs when props.count changes.
✔ Example shows how snapshot is used if available from getSnapshotBeforeUpdate().


✅ Final Interview Statement
 lll "componentDidUpdate() runs after the component re-renders due to state or prop changes.
     use for
      re-initializing libraries, 
      comparing previous props/state,


      
 



*/
