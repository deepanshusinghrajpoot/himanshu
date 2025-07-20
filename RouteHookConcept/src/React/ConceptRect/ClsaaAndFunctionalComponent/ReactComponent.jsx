import React from 'react' // imr
import StudentFunctional from '../../ConceptRect/ClsaaAndFunctionalComponent/StudentFunctional' // imp
import StudentClass from '../../ConceptRect/ClsaaAndFunctionalComponent/StudentClass'  // imp


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