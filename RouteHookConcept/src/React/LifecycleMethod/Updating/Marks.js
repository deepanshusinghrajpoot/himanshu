import React, { Component } from 'react' // ShortCut:- rcc


export default class Marks extends Component {

  constructor(props){
    super(props);
    this.state = {
        mroll: this.props.roll,
    }
  }


  static getDerivedStateFromProps(props, state){
        console.log("Updating Phase: Get Derived State from Props method before UpdatingMark");
        console.log(props, state);
        if(props.roll !== state.mroll){
            return {mroll: props.roll}
        }
       
        return null;
  }


  shouldComponentUpdate(nextProps, nextState){
        if(this.state.mroll < 107){
            console.log("Updating Phase:- shouldComponentUpdate");
            console.log(nextProps, nextState);
            return true;
        }
        console.log(nextProps, nextState);
        return false;
  }

  
  // getSnapshotBeforeUpdate() method and componentDidUpdate() are use together
  getSnapshotBeforeUpdate(prevProps, prevState){
     console.log("Updating Phase:- getSnapshotBeforeUpdate - It runs before update");
     console.log(prevProps, prevState);
     return 45; 
  }

  componentDidUpdate(prevProps, prevState, snapshot){
     console.log("Updating Phase:- componentDidUpdate - It runs after update")
     console.log(prevProps, prevState, snapshot);
  }


  render() {
    console.log("Updating Phase:- Marks - Rendered [Child of Teacher]")
    return (
      <div>
          <h1>Updating Phase:- {this.state.mroll}</h1>
      </div>
    )
  }
}
