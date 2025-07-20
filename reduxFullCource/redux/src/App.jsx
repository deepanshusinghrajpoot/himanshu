import React from 'react'
import Redux from './pages/Redux'
import Home from './pages/Home'



const App = ({store}) => {
  return (
    <div>
      <h1>App</h1>
      <Redux />
      <Home store={store} />
    </div>
  )
}

export default App