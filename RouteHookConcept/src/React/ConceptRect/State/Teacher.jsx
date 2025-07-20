import React, { Component } from 'react'

class Teacher extends Component {

    constructor(props){
        
        super(props);

        this.state = {
            name: "Himanshu Singh",
            roll: this.props.name,
        }

    }


    handleClick = () => {
        this.setState({name: "Sudhanshu Singh"});
        this.setState({roll:"109"});
    }

    render(){
        return(
            <div>
               <h3>*********** (2):- ( with Constructor ) ***********</h3>
               <h4> Hellow {this.state.name}</h4>
               <h6>Your roll numer is {this.state.roll}</h6>
               <button onClick={this.handleClick}>Change the data using state</button>
            </div>
        )
    }
}



export default Teacher