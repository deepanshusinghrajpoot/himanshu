import React from 'react'
import StudentPropsFunctional from '../../ConceptRect/Props/StudenPropsFunctional'
import StudentPropsClass from '../../ConceptRect/Props/StudentPropsClass'

const Props = () => {
  return (
    <div>
           <h1>Props Component</h1>
           <h2>================ Props ================</h2>
           <StudentPropsFunctional name="Deepanshu Singh" roll={101+2} >I am a child of functionComponent props.</StudentPropsFunctional>
           <StudentPropsClass name={"Himanshu Singh"} roll={103+1}>I am a child of classComponent props.</StudentPropsClass>
    </div>
  )
}

export default Props