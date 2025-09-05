import React, { Component } from 'react'

export default class Teacher extends Component {
    componentDidMount(){
        console.log("Unmounting Phase:- Teacher Mounted")
    }

    componentWillUnmount(){
        alert("coponentWillMount:- Teacher Unmounted");
    }
    
    render() {
        return (
          <h1>Unmounting Phase:- Hellow Teacher Component</h1>
        )
    }
}
