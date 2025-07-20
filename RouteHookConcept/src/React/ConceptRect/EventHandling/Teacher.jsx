import React from 'react'

const Student = () => {


     function handleClick(){
        console.log("button Clicked")
     }


     const handleClick2 = (e) => {
         e.preventDefault();
         console.log("go to google function component");
     }


    return (
        <div>
             <h4> Hellow Event</h4>
             <button onClick={handleClick}>Click Me</button>
             <a href="www.google.com" onClick={handleClick2} >go on google</a>
        </div>
    )
}



export default Student