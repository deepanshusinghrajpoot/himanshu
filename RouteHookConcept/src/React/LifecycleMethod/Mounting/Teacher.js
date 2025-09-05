import React, { Component } from 'react'
import Marks from './Marks'

export default class Teacher extends Component {
  render() {

    console.log("Mounting Phase:- Teacher - rendered [Child of App] ")

    return (
      <div>
        <h1>Mounting Phase:- Hello {this.props.name}</h1>
        <Marks />
      </div>
    )
  }
}
