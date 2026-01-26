import React, { Component } from 'react'


class Student extends Component {

    state = {
        name:"Deepanshu Singh",
        roll: this.props.roll,
    }

    handleClick = () => {
        this.setState({name:"Himanshu Singh"});
        this.setState({roll:"105"});
    }

    render(){
         return (
           <div>
               <h3>*********** (1):- ( without Constructor )  ***********</h3>
               <h4> Hellow {this.state.name}</h4>
               <h6>Your roll numer is {this.state.roll}</h6>
               <button onClick={this.handleClick} >Change data using state</button>
           </div>
         )
    }

}

export default Student

