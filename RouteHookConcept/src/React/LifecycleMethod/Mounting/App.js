import React, { Component } from 'react'   // sortCut:- rcc
import Teacher from './Teacher'


export default class App extends Component {
  
  constructor(props){
     super(props);   //  SubClass has reponsbility to call suber class

     console.log("Mounting Phase:- Constructor Called");
     console.log(props);

     this.state = {
        roll: "101",
     }

  }


  static getDerivedStateFromProps(props, state){
      console.log("Mounting Phase:- Get Derived State From Props method before MountingMark");
      console.log(props, state);

      return null   // App.getDerivedStateFromProps(): A valid state object (or null) must be returned. You have returned undefined.
                    // this error occur when we return undefined 
                    // mean :- if we want to change the state then retrun change state 
                    //         and if we are not change the state then return null

  }

  
  componentDidMount(){

     // Get data from server and set the data to the state 
     console.log("Mounting Phase:- componentDidMount - Mounted");

  }






  render() {

    console.log("Mounting Phase:- AppMounting - rendered");

    return (
       <div>
              <Teacher name="Rahul" />
       </div>
    )
  }

}




/*
    ======================== Print in console of brouser ====================================
        
    Mounting Phase:- Constructor Called
    {name: 'I_AM_APP_PROPS'}
    Mounting Phase:- Get Derived State From Props
    {name: 'I_AM_APP_PROPS'} {roll: '101'}
    App - rendered
    Mounting Phase:- Teacher - rendered [Child of App]
    Mounting Phase:- Marks - Rendered [Child of Teacher]
    Mounting Phase:- componentDidMount - Mounted
    

*/
