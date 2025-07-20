import React from 'react'
import Navebar from '../components/Navebar'
import { Outlet } from 'react-router-dom'

const RootLayout = () => {
  return (
    <div>
          <Navebar />
          <Outlet />  
    </div>
  )
}

export default RootLayout