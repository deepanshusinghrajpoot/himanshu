import React from 'react'


/*




//###################################################
//**************** Array method ********************* 
//###################################################

//************ how to find all method of array ***************** 
//********************************************** 
// you go to browser inspect than console
// And In console type:-  Array.prototype.
// similarly :-  function.prototype.





//************************************************* 
//**********(1) Add remove items ****************** 
//*************************************************

//************** (a) from last position ***************
//************************************************* 
// .push:- add element at the last position  of array
// .pop:-  Remove element from last position of the array
//         and return that element
  
   let number = [10, 20, 30, 40];
   console.log(`1st push item position is :- ${number.push(50)}`);
   console.log(`2nd push item position is :- ${number.push(60)}`);
   console.log(number);
                  // output:- 1st push item position is :- 5
                  //       :- 2nd push item position is :- 6
                  //       :- [10, 20, 30, 40, 50, 60]

   let popItem = number.pop();
   console.log(`pop item is:- ${popItem}`);
                  // output:- pop item is:- 60


//************** (b) from first position **************** 
//*************************************************** 
// .unshift:- add element at the first position of array
// .shift:-   remove element from first position of the array
//            and return that element

   let arr = Array(10, 20, 30, 40);
   console.log(`1st unshift item position is :- ${arr.unshift(50)} `);
   console.log(`2nd unshift item position is :- ${arr.unshift(60)}`);
   console.log(arr);
                   // output:- 1st unshift item position is :- 5
                   //       :- 2nd unshift item position is :- 6
                   //       :- [ 60, 50, 10, 20, 30, 40, ]


   let removefirst = arr.shift();
   console.log(` shift item is:- ${removefirst}`);
                   // output:-  shift item is:- 60


// *****************************************************************************************************************
// **** if add remove item from first and last position by push,pop and unshift,shift which is best performend *****
// *****************************************************************************************************************
// push,pop is best performend because :- It is not change the position(index) of other all element 
//                                mean :- not exicute left shift and right shift 
// but
// unshift,shift is not best performend because :- It is change the position(index) of other all element
//                                         mean :- exicute left shift and right shift




//***************************************************************************** 
//************ (2 :- a) slice **************** 
//*****************************************************************************
// ********** syntax(1):- arr.slice(startIndex, endIndex); :- Not including last end element(mean endIndex element)
// .slice:- It is creat a new array through by slice element

      let nnn = ["I", "love", "javascript"];
      console.log(nnn);
      let mmm = nnn.slice(1,3);
      console.log(mmm);
      console.log(nnn);
                // output:- ['I', 'love', 'javascript']
                //       :- ['love', 'javascript']
                //       :- ['I', 'love', 'javascript']

//*********** syntax(2):- arr.slice(-m); :- last position se m element is slice  
//**********************************************************************************

     let ch = ['t', 'e', 'x', 't'];
     let ccc = ch.slice(-2);
     console.log(ccc);
            // output:- ['x', 't']

// *********** syntax(3):- arr.slice(m); :- startIndex(m) to last element is slice

     let hhh = ['t', 'e', 'x', 't'];
     let cc = hhh.slice(1);
     console.log(cc);
             // output:- ['e', 'x', 't']  

//**************************************************************************
//**************** How to creat sallow copy of an array ********************
//************************************************************************** 
// sallow copy :-If any array method perform on sallow copy of array than does not effect on orignal array
// using slice method
// .slice:- arr.slice();

     let ooo = ['t', 'e', 'x', 't'];
     let oo = ooo.slice();
       oo[0] = 100;
     console.log(ooo);
     console.log(oo);
             // output:- ['t', 'e', 'x', 't']
  
     

//***************************************************************************** 
//************ (2 :- c) splice **************** 
//*****************************************************************************
// splice as:- swiss knife
// splice have many array operation :- I can do :- add, delete, replace etc.
// ***********syntax:- arr.splice(startIndex, deleteCount, arg1, arg2, arg3..............., argN)********
//                  startIndex:- start karega
//                  deleteCount:- Kitne ko delete karna hai
//                  arg1, arg2, arg3,......,argN:- delete karne ke bad inhe wha daal dega

       //******* delete and add ********* 

       let iii = ['I', 'am', 'a', 'leader'];
       let ii = iii.splice(1,2,4,5,6,7,8); //(In this case delete 2 element and add 5 element from index 1)
       console.log(ii); //(creat new array by delete)
       console.log(iii); //(after splice is performed)
       //output:- ['am', 'a']  
       //      :- ['I', 4, 5, 6, 7, 8, 'leader']

       //********** Insert *********** 

       let ppp = ['I', 'am', 'a', 'leader'];
       console.log(ppp.length);
       let pp = ppp.splice((ppp.length), 0, 10, 20, 30, 40);
       console.log(pp);
       console.log(ppp);
       //output:- 4
       //      :- []
       //      :- ['I', 'am', 'a', 'leader', 10, 20, 30, 40]

// *********** syntax(2):- arr.splice(-m); :- m is similar to 0 and m first part of splice

      let ttt = [1, 2, 3];
      let tt = ttt.splice(-1,0,4,5,6,7,8,9);
      let t = ttt.splice(-1,0,);
      console.log(t);
      console.log(tt);
      console.log(ttt);
              
              // output:- []
              //       :- [1, 2, 4, 5, 6, 7, 8, 9, 3]





//***************************************************************************** 
//************ (3) concat  **************** 
//*****************************************************************************
       let sss = [10, 20, 30, 40];
       let sns = [1, 2, 3, 4];
       let nsn = sss.concat(sns,[50, 60, 70],5 , 6, 7);
       console.log(nsn);
                  // output:- [10, 20, 30, 40, 1, 2, 3, 4, 50, 60, 70, 5, 6, 7]

  
       


//***************************************************************************** 
//************ (4) iterate **************** 
//***************************************************************************** 

//*************** foreach ***************
//*************************************** 
// ********** syntax:- arr.foreach ( function( item, index, array){        } );
//   foreach:- It is a higher order function 
//          :- because It is contain an function with arguments :- item, index, array
//                                                              :- And perform operation on argument

         let tot = [10, 20, 30, 40];
         let oto = tot.forEach(function( item, index, array){
                     console.log(`${item} is at index ${index} in ${array}`);
                  })
          // output:- 10 is at 0 in 10, 20, 30, 40
          //          20 is at 1 in 10, 20, 30, 40
          //          30 is at 2 in 10, 20, 30, 40
          //          40 is at 3 in 10, 20, 30, 40





//***************************************************************************** 
//************ (5) searching in array **************** 
//***************************************************************************** 

// ********* (a) indexof ************
// ******************************
// indexof:- using :- find index of any element in the array
       let lll = [ 1, 0, false];
       console.log(lll.indexOf(0));
       console.log(lll.indexOf(1));
       console.log(lll.indexOf(false));
       console.log(lll.indexOf(null));
       console.log(lll.indexOf(100));
             // output:- 1
             //       :- 0
             //       :- 2
             //       :- -1
             //       :- -1

// ********* (b) includes *************
// ********************************
// includes:- using :- find the element in the array
//                     In form of boolean(true or false) 
            let lsl = [ 1, 0, false];
            console.log(lsl.includes(0));
            console.log(lsl.includes(1));
            console.log(lsl.includes(false));
            console.log(lsl.includes(null));
            console.log(lsl.includes(100));
            // output:- true
            //       :- true
            //       :- true
            //       :- false
            //       :- false

//************ (c) find **************** 
//***************************************************************************** 
//****** syntax:- arr.find( function( item ){       });
//  find:- It is a higher order function 
//      :- because it is contain an argument :- item 
//                                           :- :- And perform operation on orgument 

     let users = [
                { id:'1', Name:'deepanshu'},
                { id:'2', Name:'himanshu'},
                { id:'3', Name:'ankit'},
                { id:'4', Name:'appu'}
              ]
     let user = users.find(function(item){  
                            
                        return  item.id == 1 ;
                                 
                    })
     console.log(user);
     // output:- { id:'1', Name:'deepanshu'}           
 

//************ (d) findindex **************** 
//***************************************************************************** 
//****** syntax:- arr.findindex( function( index ){       });
//  find:- It is a higher order function 
//      :- because it is contain an argument :- index
//                                           :- :- And perform operation on orgument 

        let sst = [
                 { id:'1', Name:'DEEPANSHU'},{id:'3', Name:'HIMANSHU'},
                 { id:'2', Name:'ANKIT'},{id:'4', Name:'APPU'}
              ];
        let tss = sst.findIndex(function(index){
                              return  index.Name == "pintu";
                           })
            console.log(tss);
            // output:- -1




//***************************************************************************** 
//************ (e) reverse **************** 
//***************************************************************************** 
// reverse :- It is reverse the array
     let nnnn = [ 1, 2, 3, 4, 5 ];
     nnnn.reverse();
     console.log(nnnn);
     // output :- [ 5, 4, 3, 2, 1 ]




//***************************************************************************** 
//************ (6) split **************** 
//***************************************************************************** 
// split :- It is split any thing(eg:- string) and convert into an array
//       :- split is according to an major point
// major point :- obtain according to you
//  eg:- you send message n number of candident THAN
 
          let names = 'deepanshu,himanshu,ankit,appue';
          let arrr = names.split(',');
          console.log(arrr);
          for(let i of arrr){
               console.log(`Hello ${i} Happy holi your life is bring to color`);
          }
          // output:- Hello deepanshu Happy holi 
          //          your life is bring to color
          //       :- Hello himanshu Happy holi 
          //          your life is bring to color
          //       :- Hello ankit Happy holi 
          //          your life is bring to color
          //       :- Hello appue Happy holi 
          //          your life is bring to color



//***************************************************************************** 
//************ (7) join **************** 
//***************************************************************************** 
// join :- It is join any thing(eg:- string) and convert into an single string
//       :- join is according to an major point
// major point :- obtain according to you
//  eg:- you send message n number of candident 
//       and find the name from all message and
//       convert the all name of user into an single string
        let mssm = ['deepanshu','himanshu','ankit','appu'];
        let smms = mssm.join(":");
        console.log(smms);
        // output:- deepanshu:himanshu:ankit:appu

 





 */



const ArrayMethods = () => {
  return (
    <div>ArrayMethods</div>
  )
}

export default ArrayMethods