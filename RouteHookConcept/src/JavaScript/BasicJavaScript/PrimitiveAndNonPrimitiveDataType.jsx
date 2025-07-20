import React from 'react'

/*



✅ Summary
Data Type = Kind of data stored (String, Number, Object, etc.)
Variable = Container to hold data (declared with var, let, const)







✅ Primitive Data Types (Value Types)
Stored directly in the stack memory
Immutable (cannot be changed after creation)
Compared by value
Copy creates a new independent value




🔥 List of Primitive Types:
Data Type                                    Example
String	                                     "Hello World"
Number	                                     42, 3.14, -7
Boolean	                                     true, false
Undefined	                                   let x; → x is undefined
Null	                                       let y = null;
Symbol	                                     Symbol("id")
BigInt	                                     123456789n

nnnssbb


✅ Example:

let a = 10;
let b = a;
b = 20;

console.log(a);  // 10
console.log(b);  // 20

✔ a and b hold independent copies









✅ Non-Primitive (Reference) Data Types
Stored in heap memory
Mutable (can change the contents)
Compared by reference (memory address)
Copy holds reference, not the actual value



🔥 Examples of Non-Primitive Types:
Data Type	                            Example
Object	                                { name: "Deepanshu" }
Array	                                [1, 2, 3]
Function	                            function() {}
Date	                                new Date()
RegExp	                                /abc/







✅ Example:

let obj1 = { name: "Deepanshu" };
let obj2 = obj1;

obj2.name = "Himanshu";

console.log(obj1.name);  // Himanshu
console.log(obj2.name);  // Himanshu

✔ Both obj1 and obj2 point to the same memory







⚡️ Quick Interview Summary


✅ Primitive Data Types

        Stored in stack
        Immutable
        Compared by value



✅ Non-Primitive (Reference) Types

        Stored in heap
        Mutable
        Compared by reference



        
*/







const PrimitiveAndNonPrimitiveDataType = () => {
  return (
    <div>PrimitiveAndNonPrimitiveDataType</div>
  )
}

export default PrimitiveAndNonPrimitiveDataType