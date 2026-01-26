import React, { Component } from 'react' // rcc

export default class StudentClass extends Component {
  render() {
    return (
      <div>
        <h3>****************** Class Component *****************************</h3>
        <h6>This is a class component And {this.props.name}</h6>
      </div>
    )
  }
}


