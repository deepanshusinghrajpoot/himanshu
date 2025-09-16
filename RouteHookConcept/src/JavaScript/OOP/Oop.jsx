import React from 'react'




/*


what is object
--------------

object :- A javascript object is an entity having state and behavior (properties and method).



In javaScript there are two way creating object
-----------------------------------------------

(1). Direct way of creating object
--------------------------------

const obj = {
    firstName:"Deepanshu Singh",
    greet: function () {
        console.log(this.firstName);
    }
}



(2). Using classes creating object
----------------------------------


class :- class is blue print that define property and behaviour


class ToyotaCar{

      start(){
        console.log("Start");
      }

      stop(){
        console.log("stop");
      }

      setBrand(brand){
        this.brand = brand;
      }
  }



  let fortuner = new ToyotaCar();
  fortuner.setBrand("fortuner");

  let lexus = new ToyotaCar();
  fortuner.setBrand("fortuner");





  What is Constructor in javaScript
  ----------------------------------

 Constructor
-----------

Special method invoked automatically at time of object creation. Used for Initialization.


       properties
       ----------

       1. Constructor have Same name as class
       2. Constructor doesn't have a return type
       3. Constructor is called only once (automaticaly), at object creation
            if we are not make constructor, compiler make default constructor automaticaly.
       4. Memory allocation happens when constructor is called
          So,
            Memory allocation is happen for object not for class.
            







 */















const Oop = () => {


  class ToyotaCar{

      constructor(company){
         this.company = company;
         console.log("Creating new object");
      }

      start(){
        console.log("Start");
      }

      stop(){
        console.log("stop");
      }

      setBrand(brand){
        this.brand = brand;
      }
  }



  let fortuner = new ToyotaCar();
  fortuner.setBrand("fortuner");

  let lexus = new ToyotaCar();
  fortuner.setBrand("fortuner");



  return (
    <div>Oop</div>
  )
}

export default Oop