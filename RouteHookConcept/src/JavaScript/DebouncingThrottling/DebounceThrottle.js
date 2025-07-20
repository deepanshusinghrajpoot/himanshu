
/*


file:- index.html




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
      <h1>Debouncing and Throttling</h1>
      <button class="click_btn" > click </button>
      <div> key Stroke <span class="keyCounter"></span> </div>
      <div> Debounce effect <span class="debounce_effect"></span></div>
      <div> Throttling effect <span class="throttle_effect"></span></div>


      <script src="./test.js"></script>
</body>
</html>








 file :- test.js
--------------------


 

const btn = document.querySelector(".click_btn");
const keyCounter = document.querySelector(".keyCounter");
const debounceEffect = document.querySelector(".debounce_effect");
const throttleEffect = document.querySelector(".throttle_effect");


let count = 0;
let debounceEffectCount = 0;
let throttleEffectCount = 0;



function debouncing(fn, delay){   
    let timer;
    return function (...args) {     
         let context = this;
         clearTimeout(timer);
         timer = setTimeout(()=>{
            fn.apply(context, args);
         }, delay)
    }
}



function throttling(fn, limit){
    let flag = true;
    return function (...args) {
        let context = this;
        if(flag){
            fn.apply(context, args);
            flag = false;
            setTimeout(()=>{
                flag = true;
            }, limit)
        }
    }
}




const x = () => {
    debounceEffect.innerHTML = ++debounceEffectCount;
}

const y = () => {
    throttleEffect.innerHTML = ++throttleEffectCount;
}



const debounceFunction = debouncing(x, 5000);
const throttleFunction = throttling(y, 5000);




btn.addEventListener("click", ()=>{
    keyCounter.innerHTML = ++count;
    throttleFunction();
    debounceFunction()
})











*/