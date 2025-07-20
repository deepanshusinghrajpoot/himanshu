import React from 'react'


/*


🔥 Map, Filter, Reduce in JavaScript — Best Practice Guide




✅ 1. map() — Transform an Array
map() creates a new array by applying a function to each element of the original array.


const arr = [5, 1, 3, 2, 6];

// Example - Convert numbers to binary string
const output = arr.map((x) => x.toString(2));

console.log(output); 
// Output: ["101", "1", "11", "10", "110"]






✅ 2. filter() — Filter Values Based on Condition
Returns a new array containing elements that satisfy the condition (returns true).


const arr = [5, 1, 3, 2, 6];

// Filter odd numbers
const output1 = arr.filter((x) => x % 2 !== 0);
console.log(output1); 
// Output: [5, 1, 3]

// Filter even numbers
const output2 = arr.filter((x) => x % 2 === 0);
console.log(output2); 
// Output: [2, 6]






✅ 3. reduce() — Reduce Array to a Single Value
Combines all array values into a single result (sum, max, counts, etc.).




const arr = [5, 1, 3, 2, 6];

// Sum of array
const sum = arr.reduce((acc, curr) => acc + curr, 0);
console.log(sum); 
// Output: 17



// Find maximum element
const max = arr.reduce((acc, curr) => (curr > acc ? curr : acc), arr[0]);
console.log(max); 
// Output: 6








✅ Real World Example — Combine map, filter, reduce


const users = [
    { firstName: "Deepanshu", lastName: "Singh", age: 26 },
    { firstName: "Donald", lastName: "Trump", age: 75 },
    { firstName: "Elon", lastName: "Musk", age: 50 },
    { firstName: "Deepika", lastName: "Padukone", age: 26 },
];







🔹 Full Name List using map()
const fullNames = users.map((user) => `${user.firstName} ${user.lastName}`);
console.log(fullNames); 
// Output: ["Deepanshu Singh", "Donald Trump", "Elon Musk", "Deepika Padukone"]







🔹 Age Frequency Count using reduce()
const ageCount = users.reduce((acc, curr) => {
    acc[curr.age] = (acc[curr.age] || 0) + 1;
    return acc;
}, {});

console.log(ageCount); 
// Output: {26: 2, 75: 1, 50: 1}
✅ Step-by-Step:

If age exists in acc, increment it.
If not, initialize with 1.







🔹 First Names of Users Age < 30 using filter() and map()

const youngUsers = users
    .filter((user) => user.age < 30)
    .map((user) => user.firstName);

console.log(youngUsers); 
// Output: ["Deepanshu", "Deepika"]






🔹 Same Task using Only reduce()

const youngUsers2 = users.reduce((acc, curr) => {
    if (curr.age < 30) acc.push(curr.firstName);
    return acc;
}, []);

console.log(youngUsers2); 
// Output: ["Deepanshu", "Deepika"]



*/



const MapFillterReduce = () => {
  return (
    <div>MapFillterReduce</div>
  )
}

export default MapFillterReduce