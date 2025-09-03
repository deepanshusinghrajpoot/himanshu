import React from 'react'
import StudentState from '../../ConceptRect/State/Student'
import TeacherState from '../../ConceptRect/State/Teacher'



const State = () => {
  return (
    <div>
        <h1>State</h1>
        <StudentState roll="101" />
        <TeacherState name="Deepanshu Singh" />
    </div>
  )
}

export default State