import React from 'react'

/*


⭐ What is React Router?
✅ React Router is a standard routing library for React that enables navigation between different components in a React application 
    without reloading the entire page, creating a smooth Single Page Application (SPA) experience.



    
✅ Key Features of React Router
Handles Client-side Routing, updating the URL and component view without a full page refresh.
Supports Dynamic Routing, where routes can be generated based on application state.
Enables Nested Routing, allowing routes within routes for building complex layouts.
Helps manage browser history with history API.
Works for both Web and Mobile (with React Native).





⭐ How to Implement React Router in a React Project


✅ Step 1: Install React Router

npm install react-router-dom





✅ Step 2: Wrap Application with BrowserRouter In main.jsx or index.js:

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { BrowserRouter } from 'react-router-dom';

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);





✅ Step 3: Define Routes in App.jsx

import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import About from './About';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about' element={<About />} />
      </Routes>
    </>
  );
}

export default App;





✅ Step 4: Navigation using Link

import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
    </nav>
  );
}

export default Navbar;




⭐ Important Notes
✔ BrowserRouter must wrap your application for routing to work.
✔ Use Link instead of <a> to avoid full page reloads.
✔ The path prop defines the URL route, element defines which component renders.
✔ Supports nested and dynamic routes.




*/



const Route = () => {
  return (
    <div>RouteOld</div>
  )
}

export default Route