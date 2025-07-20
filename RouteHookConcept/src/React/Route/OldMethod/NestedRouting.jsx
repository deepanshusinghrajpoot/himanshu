import React from 'react'





/*

⭐ React Router — Nested Routes


✅ Nested Routes (Child Routes)
We use nested routes to render components inside other components based on the URL structure.

Example:


-------App.jsx--------

import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import About from './About';
import Dashboard from './Dashboard';
import Profile from './Profile';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="about" element={<About />} />

      {/* Parent Route }
      <Route path="dashboard" element={<Dashboard />} >
        {/* Child Route }
        <Route path="profile" element={<Profile />} />
      </Route>
    </Routes>
  );
}






---------- Dashboard.jsx ----------

import { Outlet, Link } from 'react-router-dom';

function Dashboard() {
  return (
    <div>
      <h1>Dashboard Page</h1>
      <Link to="profile">Go to Profile</Link>

      {/* Outlet will render child routes }
      <Outlet />
    </div>
  );
}

export default Dashboard;


✔ Now when user goes to /dashboard/profile, both Dashboard and Profile will render, thanks to <Outlet />.




*/












const NestedRouting = () => {
  return (
    <div>NestedOld</div>
  )
}

export default NestedRouting