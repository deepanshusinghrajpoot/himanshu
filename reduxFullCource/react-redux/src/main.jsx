import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { applyMiddleware, combineReducers, createStore } from 'redux';
import { accountReducer } from './reducers/account';
import { bonusReducer } from './reducers/bonus';
import logger from 'redux-logger';
import { thunk } from 'redux-thunk';
import {Provider} from 'react-redux'


const store = createStore(
  combineReducers({
      account: accountReducer,
      bonus: bonusReducer,
  }),
  applyMiddleware(logger, thunk)

); // applyMiddleware is used to add middleware to the store, in this case, we are using logger middleware to log the actions and state changes to the console.







createRoot(document.getElementById('root')).render(
  <StrictMode>
      <Provider store={store} >
           <App />
      </Provider>
  </StrictMode>,
)
