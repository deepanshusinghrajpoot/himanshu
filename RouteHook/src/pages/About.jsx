import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { withAuth } from '../utils/HOC/withAuth';

const About = (data) => {

   
  const navigate = useNavigate();

  const {name, height} = data;

  return (
    <div>
        <h1>About page</h1>
        <h2>Brother Name:{name}</h2>
        <h2>Height:{height}</h2>
        <div className='navbar'>
            <ul>
                <li onClick={()=> navigate('useState')} style={{cursor:'pointer'}} >1. useState</li>
                <li onClick={()=> navigate('useEffect')} style={{cursor:"pointer"}} >2. useEffect</li>
                <li onClick={()=> navigate('useRef')} style={{cursor:"pointer"}} >3. useRef</li>
                <li onClick={()=> navigate('useMemo')} style={{cursor:'pointer'}} >4. useMemo</li>
                <li onClick={()=> navigate('useCallback')} style={{cursor:'pointer'}} >5. useCallback</li>
                <li>6. useContext see in the frontend folder</li>
                <li onClick={()=> navigate('useReducer')} style={{cursor:'pointer'}} >7. useReducer</li>
                <li onClick={()=> navigate('useLayoutEffect')}  style={{cursor:'pointer'}} >8. useLayoutEffect</li>
                <li onClick={()=> navigate('customHook') } style={{cursor:'pointer'}} >9. customHook</li>  
            </ul>
        </div> 
    </div>
  )
}





export default About
