import React from 'react'

const Header1 = () => {
  
  console.log("Header Redered Header 1 !");

  return (
    <div>
        <p>This is a Header 1</p>
    </div>
  )
}


// React.memo is a higher-order component that prevents unnecessary re-renders.
// It re-renders the component only when its props change, not when parent re-renders.

export default React.memo(Header1)