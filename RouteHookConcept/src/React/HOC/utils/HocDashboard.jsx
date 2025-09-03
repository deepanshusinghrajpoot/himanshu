import React from "react";
import { withAuth } from "./withAuth";




const HocDashboard = ({username}) => {
    return (
        <h1>Hellow {username} you are login, Now you can access the dashbord</h1>
    )
}



const ProtectedHocDashboard = withAuth(HocDashboard);


export default ProtectedHocDashboard;
