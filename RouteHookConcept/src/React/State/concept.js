/*


✅ State in React
State is similar to props, but:
State is private and controlled by the component itself.
Props are passed from parent to child and are read-only.
State can be updated, props cannot (directly).



✅ Where Can You Use State?
Component Type	State Support
Class Component	                                        ✅ Yes
Functional Component	                                     ✅ Yes (using Hooks, e.g., useState)
Older versions (< React 16.8)	Only class components



✅ Two Ways to Initialize State (Class Components):

1️⃣ Without Constructor (Modern Way):

class Student extends React.Component {
  state = {
    name: "Deepanshu Singh",
    prop1: this.props.prop1
  };

  render() {
    return <h1>{this.state.name}</h1>;
  }
}
✅ Note: Cleaner syntax. No need to use constructor or super().

2️⃣ With Constructor (Traditional Way):

class Student extends React.Component {
  constructor(props) {
    super(props);  // must call parent constructor
    this.state = {
      name: "Himanshu Singh",
      prop1: this.props.prop1
    };
  }

  render() {
    return <h1>{this.state.name}</h1>;
  }
}
✅ Why call super(props)?

Makes this.props available inside the constructor.

✅ Updating State (Class Components):
Use this.setState() method — this triggers a re-render.

this.setState({ name: "New Name" });
❌ You should not mutate state directly like this.state.name = "abc".

📝 Summary Table:
Aspect	Explanation
props	Data passed from parent, read-only
state	Local data, private to component, can be updated
setState()	Method to update state and re-render UI

*/