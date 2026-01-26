import React from 'react'

const StudentPropsFunctional = (props) => {
    return (
        <div>
            <h3>*********************** Props using functionalComponent **************************</h3>
            <h6>This is a props understanding describe by Name:{props.name} roll:{props.roll}</h6>
            <h4>{props.children}</h4>
        </div>
    )
}

export default StudentPropsFunctional