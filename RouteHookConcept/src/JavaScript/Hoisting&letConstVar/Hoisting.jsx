import react from 'react';

/*

Interview-Ready Explanation:

✅ What is Hoisting?
lll Hoisting is JavaScript's default behavior where variable and function declarations are moved to the top of their scope during the memory creation phase of the Global Execution Context (GEC).


Step-by-Step Technical Breakdown:

✔ function getName() is hoisted with its definition, so calling getName() before declaration works.
✔ var getName1 is hoisted but initialized as undefined, so calling getName1() before assignment gives TypeError, because undefined is not callable.
✔ var x is hoisted, initialized as undefined, so console.log(x) prints undefined.
✔ console.log(getName) prints the full function definition because function declarations are fully hoisted.

Final Interview-Style Statement:
"In JavaScript, during the creation phase of Global Execution Context, memory is allocated for variables (var as undefined) and for function declarations with their actual code.
This behavior is called Hoisting. But function expressions like var getName1 = () => {} are treated as variables, so accessing them before initialization results in TypeError."

*/


const Hoisting = () => {
   
   // Corrected Code and Output:

     getName();    // Namaste India
     getName1();   // TypeError: getName1 is not a function
     console.log(x);  // undefined
     console.log(getName);  // [Function: getName]

     var x = 7;

     function getName() {
          console.log("Namaste India");
     }

     var getName1 = () => {
         console.log("Namaste India 2");
     };


     return( 
        <div>
            <h1>Hoisting</h1>
        </div>
     )

}



export default Hoisting;













/*

var x = 1; 

a();
b();

console.log(x);

function a(){
    var x = 10;
    console.log(x);
}

function b(){
   var x = 100;
   console.log(x); 
}


output 10
       100
       1

✅ Refined Memory Diagram:

Global Memory:
-----------------
x → undefined  → after assignment → 1
a → function reference
b → function reference
When a() runs:


a's Local Memory:
------------------
x → undefined → 10
When b() runs:


b's Local Memory:
------------------
x → undefined → 100


*/