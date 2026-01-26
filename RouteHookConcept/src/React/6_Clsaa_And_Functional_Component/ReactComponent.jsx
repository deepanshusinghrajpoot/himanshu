import React from 'react' // imr
import StudentFunctional from './StudentFunctional' // imp
import StudentClass from './StudentClass'  // imp


const ReactComponent = () => {

    return (
        <div>
            <h1>React Component</h1>
            <StudentFunctional name='Deepanshu Singh explain functional component' />
            <StudentClass name="Deepanshu Singh explain class component" />
        </div>
    )
}



export default ReactComponent