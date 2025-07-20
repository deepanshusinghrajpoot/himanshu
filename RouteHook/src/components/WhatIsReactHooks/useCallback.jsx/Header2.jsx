import React from 'react'

const Header2 = () => {
    console.log("Header Redered Header 2 !");

    return (
      <div>
          <p>This is a Header 2</p>
      </div>
    )
}

export default React.memo(Header2)