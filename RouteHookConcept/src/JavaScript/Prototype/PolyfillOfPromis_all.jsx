import React from 'react'


/*


V.V.V.important for fresher and intermidiate level interview
------------------------------------------------------------



Promise.allPromis = function (promise) {

    return new Promise((resolve, reject) => {
           
          let result = [];


          if(!promise.length){
            resolve(result);
            return;
          }

          let pending = promise.length;

          promise.map((promis, index)=>{
               Promise.resolve(promis).then((res) => {
                   
                     result[index] = res;
                     pending--;

                     if(pending === 0){
                        resolve(result);
                     }
               }, reject );
          })

    })
} 






let p1 = new Promise ((resolve, reject) => {

    setTimeout(()=>{
        resolve("Deepanshu Singh");
    }, 2000);

})



let p2 = new Promise ((resolve, reject) => {

    setTimeout(()=>{
        reject(5000);
    }, 1000);

})


let p3 = new Promise ((resolve, reject) => {

        resolve("Himanshu Singh");
    
})




const all =  Promise.allPromis([p1, p2, p3]);
all.then((res) => console.log("allPromis resolve :- ", res)).catch((err) => console.log("allPromis rejected :- ", err));






*/




const PolyfillOfPromis_all = () => {

  
Promise.allPromis = function (promise) {

    return new Promise((resolve, reject) => {
           
          let result = [];


          if(!promise.length){
            resolve(result);
            return;
          }

          let pending = promise.length;

          promise.map((promis, index)=>{
               Promise.resolve(promis).then((res) => {
                   
                     result[index] = res;
                     pending--;

                     if(pending === 0){
                        resolve(result);
                     }
               }, reject );
          })

    })
} 






let p1 = new Promise ((resolve, reject) => {

    setTimeout(()=>{
        resolve("Deepanshu Singh");
    }, 2000);

})



let p2 = new Promise ((resolve, reject) => {

    setTimeout(()=>{
        reject(5000);
    }, 1000);

})


let p3 = new Promise ((resolve, reject) => {

        resolve("Himanshu Singh");
    
})




const all =  Promise.allPromis([p1, p2, p3]);
all.then((res) => console.log("allPromis resolve :- ", res)).catch((err) => console.log("allPromis rejected :- ", err));



  return (
    <div><h1>Polyfill of Promis.all([]) method</h1></div>
  )


}

export default PolyfillOfPromis_all