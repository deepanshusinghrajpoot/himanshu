import React, { Component } from 'react'

export default class Marks extends Component {
  render() {
    
    console.log("Mounting Phase:- Marks - Rendered [Child of Teacher]")

    return (
      <div>
           <h1>Mounting Phase:- Marks Component</h1>
      </div>
    )
  }
}
