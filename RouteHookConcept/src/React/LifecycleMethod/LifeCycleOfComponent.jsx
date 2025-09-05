import React from 'react'

const LifeCycleOfComponent = () => {
  
  const handleClick = (e, value) => {
        console.log(e);
        alert(value); 
  }

  return (
    <div>
        <p>LifeCycleOfComponent Present in separet project because life cycle methode access only in side clase component.</p>
        <button onClick={(e)=> handleClick(e, "Deepanshu are You Learn Life Cycle Method of Component") }>Click Handle</button>
    </div>
  )
}

export default LifeCycleOfComponent