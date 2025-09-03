/*



✅ React Props (Properties)
When React renders a user-defined component, it passes JSX attributes to this component as a single object called props.



✅ Example:

const Student = (props) => {
  return (
    <div>
      <p>Hello, {props.name}</p>
      <p>Roll No: {props.roll}</p>
    </div>
  );
};

ReactDOM.render(<Student name="Deepanshu" roll="101" />, document.getElementById("root"));
You can pass:

String: <Student name="Deepanshu" />

JavaScript Expression: <Student roll={101 + 1} />

✅ Important Notes:
If you pass no value to a prop (e.g., <Button disabled />), it defaults to true.

Components should never modify their own props. They must act like pure functions with respect to props.

✅ Pure vs Impure Function:
Type	Example
Pure Function	function sum(a, b) { return a + b; }
Impure Function	function withdraw(account, amount) { account.total -= amount; return account; }

✅ props.children in JSX
When you write:

<Student>Hello World</Student>
The Hello World text is available via props.children.

Example:

const Student = (props) => {
   return (
     <div>
       {props.children}
     </div>
   );
};



✅ Summary Points:
Props are inputs to components (read-only).
Props make components reusable.
Children allow you to nest elements inside components.
Use props to pass dynamic data.




*/