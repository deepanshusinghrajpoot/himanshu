import React from 'react'

const Header1 = () => {
  
  console.log("Header Redered Header 1 !");

  return (
    <div>
        <p>This is a Header 1</p>
    </div>
  )
}

// memo is a react method which is allow to redere the component when chage the state of this component
export default React.memo(Header1)