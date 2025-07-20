import React from 'react'
import { assets } from '../../../frontend/src/assets/assets'
import { Link, NavLink } from 'react-router-dom'

const Navebar = () => {
  return (
    <div className='navbar' >
        <img src={assets.logo} alt="" style={{width:'2.5rem'}} />
        <ul>
            <NavLink to='/' ><li>Home</li></NavLink>
            <NavLink to='/about' ><li>About</li></NavLink>
            <NavLink to='/products' ><li>Products</li></NavLink>
            <NavLink to='/contact' ><li>Contact</li></NavLink>
        </ul>
        <button>Gets Started</button>
    </div>
  )
}

export default Navebar