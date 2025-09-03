import react from 'react';
import ProtectedHocDashboard from './HocDashboard';



const HOC = () => {
     
    return (
        <ProtectedHocDashboard  isAuthenticated={true} username="Deepanshu" />
    )

}



export default HOC;