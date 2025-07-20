import React, { Component } from 'react'



class Student extends Component{

    handleClick = () => {
        console.log("buttonClick", this);
    }


    handleClick2 = (e) => {
        e.preventDefault();
        console.log("go to goosle class component");
    }


    render(){
        return(
            <div>  
                   <h4> Hellow Event</h4>
                   <button onClick={this.handleClick}>Click Me</button>
                   <a href="www.google.com" onClick={this.handleClick2} >go to google</a>
            </div>
        )
    }
}


export default Student