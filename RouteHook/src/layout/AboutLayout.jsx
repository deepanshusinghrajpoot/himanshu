import React from 'react'
import About from '../pages/About'
import { Outlet } from 'react-router-dom'
import { withAuth } from '../utils/HOC/withAuth'
import { withDarkMode } from '../utils/HOC/withDarkMode'


const AboutLayout = () => {

  const data = {name:"Himanshu Singh", height:"6fit"}

  const AuthAbout = withAuth(About);

  return (
    <div>
        <AuthAbout />
        <Outlet />
    </div>
  )
}

export default AboutLayout