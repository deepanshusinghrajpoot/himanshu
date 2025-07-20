import React, { Component } from 'react'


export default class StudentPropsClass extends Component {
    render(){
      return (<div>
                      <h3>*********************** Props using classComponent **************************</h3>
                      <h6>This is a props understanding describe by Name:{this.props.name} roll:{this.props.roll}</h6>
                      <h4>{this.props.children}</h4>
              </div>)
    }
}



