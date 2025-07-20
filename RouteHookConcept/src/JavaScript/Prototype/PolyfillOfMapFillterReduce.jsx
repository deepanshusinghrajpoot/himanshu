import React from 'react'


/*

1.  Polyfill for map()
    Array.map((num, i, arr) => {})


// arr.myMap() here inside myMap function this point to the arr
// inside the function :-   this = arr


let arr = [1, 2, 3, 4, 5];



✅ 1. map() – Your Polyfill (Correct ✅)

Array.prototype.myMap = function (cb) {

  let temp = [];
  for (let i = 0; i < this.length; i++) {
    temp.push(cb(this[i], i, this));
  }
  return temp;

};

let myMapArr = arr.myMap((num, i, arr) => num * 3);
console.log("Polyfill of map:", myMapArr); // [3, 6, 9, 12, 15]










2.   Polyfill for filter()
     arr.filter((num, i, arr) => {})


✅ Polyfill for filter()

Array.prototype.myFilter = function (cb) {
  let temp = [];

  for (let i = 0; i < this.length; i++) {
    if (cb(this[i], i, this)) {
      temp.push(this[i]); // ✅ push the actual element, not cb()
    }
  }

  return temp;
};

let myFilterArr = arr.myFilter((num) => num > 2);
console.log("Polyfill for filter:", myFilterArr); // [3, 4, 5]











3.  Polyfill for reduce()
    arr.reduce((acc, curr, i, arr) => {}, initialValue);



✅ Polyfill for reduce()

Array.prototype.myReduce = function (cb, initialValue) {
  let accumulater = initialValue;
  let startIndex = 0;

  if (initialValue === undefined) {
    accumulater = this[0];
    startIndex = 1;
  }

  for (let i = startIndex; i < this.length; i++) {
    accumulater = cb(accumulater, this[i], i, this);
  }

  return accumulater;
};

let myReduceArr = arr.myReduce((acc, curr) => acc + curr, 5);
console.log("Polyfill for reduce:", myReduceArr); // 20





*/




const PolyfillOfMapFillterReduce = () => {

  return (
    <div><h1>PolyfillOfMapFillterReduce</h1></div>
  )

}

export default PolyfillOfMapFillterReduce
