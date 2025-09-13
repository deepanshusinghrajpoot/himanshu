import { StrictMode, Suspense } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import ContextProvider from './context/AppContext.jsx'
import {BrowserRouter} from 'react-router-dom'
import { Provider } from 'react-redux'
import store from './redux/Store.jsx'


createRoot(document.getElementById('root')).render(
  
<BrowserRouter>
  <Provider store={store}>
    <ContextProvider>
          <Suspense  fallback={<h1>Loading...</h1>} >
                <App /> 
          </Suspense>
    </ContextProvider>
  </Provider>
</BrowserRouter>
  
)
