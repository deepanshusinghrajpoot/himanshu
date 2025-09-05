import React, { Component } from 'react' // shortCut:- rcc
import Teacher from './Teacher';

export default class AppUnmount extends Component {
  
  constructor(){
    super()

    this.state = {
      status:true,
    }
  }


  componentDidMount(){
    console.log("Unmounting Phase:- Appmounted");
  }
  
  componentWillUnmount(){
     console.log("Unmounting Phase:- AppUnmounted");
  }


  render() {
    return (
       <div>
           <h1>Unmounting Phase:- AppUnmounted Component</h1>
           {
             this.state.status ? <Teacher /> : <h1>Teacher component is remove from DOM</h1>
           }
           <button onClick={()=> this.setState({status: !this.state.status}) } >Click</button>
       </div>
    )
  }
}
