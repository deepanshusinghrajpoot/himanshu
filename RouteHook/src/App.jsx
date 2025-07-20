import React from 'react'
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from 'react-router-dom'
import RootLayout from './layout/RootLayout'
import Products from './pages/Products'
import ContactLayout from './layout/ContactLayout'
import ContactInfo from './components/ContactInfo'
import ContactForm from './components/ContactForm'
import NotFound from './components/NotFound'
import UseState from './components/WhatIsReactHooks/useState/UseState'
import UseEffect from './components/WhatIsReactHooks/useEffect/UseEffect'
import UseRef from './components/WhatIsReactHooks/useRef/UseRef'
import UseMemo from './components/WhatIsReactHooks/useMemo/UseMemo'
import UseCallback from './components/WhatIsReactHooks/useCallback.jsx/UseCallback'
import UseReducer from './components/WhatIsReactHooks/useReducer/UseReducer'
import UseLayoutEffect from './components/WhatIsReactHooks/useLayoutEffect/UseLayoutEffect'
import CustomHook from './components/WhatIsReactHooks/CustomHook/CustomHook'
import JobsLayout from './layout/JobsLayout'
import Jobs from './pages/Jobs'
import Home from './pages/Home'
import AboutLayout from './layout/AboutLayout'




const App = () => {

 const router = createBrowserRouter(
    createRoutesFromElements(
       <Route path='/' element={<RootLayout />} >
          <Route index element={<Home />} />
          <Route path='about' element={<AboutLayout />} >
               <Route path='useState' element={<UseState />} />
               <Route path='useEffect' element={<UseEffect />} />
               <Route path='useRef' element={<UseRef />} />
               <Route path='useMemo' element={<UseMemo />} />
               <Route path='useCallback' element={<UseCallback />} />
               <Route path='useReducer' element={<UseReducer />} />
               <Route path='useLayoutEffect' element={<UseLayoutEffect />} />
               <Route path='customHook' element={<CustomHook />} />
          </Route>
          <Route path='products' element={<Products />} />
          <Route path='contact' element={<ContactLayout />}>
                <Route path='info' element={<ContactInfo />} />
                <Route path='form' element={<ContactForm />} />
          </Route>
          <Route path='jobs' element={<JobsLayout />} >
               <Route index element={<Jobs />} />
          </Route>
          <Route path='*' element={<NotFound />} />
       </Route>
    )
 )



  return (
     <RouterProvider router={router} />
  )
}

export default App
