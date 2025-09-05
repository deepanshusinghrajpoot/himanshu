import React, { Component } from 'react' // ShortCut:- rcc
import Marks from './Marks';


export default class Teacher extends Component {
  
  // for making state not compulsory to make constructor

  constructor(){   
     super();

     this.state = {
        roll: 101,
     }
  }


  clickHandle = () => {
      console.log("Button Clicked");
      this.setState({roll:this.state.roll + 2});
  }


  render() {
    console.log("========== Updating Phase ==============");
    console.log("Updating Phase:- TeacherMounting - Rendered")
    return (
      <div>
           <Marks roll={this.state.roll} />
           <button onClick={this.clickHandle} >Updating Phase:- Change</button>
      </div>
    )
  }

}
