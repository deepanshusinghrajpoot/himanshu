/*




🔹 Controlled Components (Interview Answer)
----------------------------------------------
What I’ll say to the interviewer 👇

lll “In React, a controlled component is a form element whose value is fully controlled by React state.
The input value comes from useState, and every change is handled using an onChange handler.
This gives React complete control over the form data.”



✅ Example (Controlled Component)
----------------------------------

import { useState } from "react";

function ControlledForm() {
  const [name, setName] = useState("");

  return (
    <input
      type="text"
      value={name}
      onChange={(e) => setName(e.target.value)}
    />
  );
}

🧠 Key Points to Mention

Value is stored in React state
value + onChange are required
Easy to validate, manipulate, and submit
Preferred in real-world React apps








🔹 Uncontrolled Components (Interview Answer)
=================================================
What I’ll say to the interviewer 👇

“An uncontrolled component is a form element where React does not control the input value.
Instead, the form data is handled by the DOM itself, and we access it using a ref.”



✅ Example (Uncontrolled Component)
------------------------------------

import { useRef } from "react";

function UncontrolledForm() {
  const inputRef = useRef();

  const handleSubmit = () => {
    console.log(inputRef.current.value);
  };

  return (
    <>
      <input type="text" ref={inputRef} />
      <button onClick={handleSubmit}>Submit</button>
    </>
  );
}










*/