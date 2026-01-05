import React from 'react'


/*


/*
✅ Route Parameters (Dynamic Routes)
Useful to send dynamic values through URL (e.g., user IDs, product IDs).

Example:




--------App.jsx----------

import { Routes, Route } from 'react-router-dom';
import User from './User';

function App() {
  return (
    <Routes>
      <Route path="user/:id" element={<User />} />
    </Routes>
  );
}




---------User.jsx-----------

import { useParams } from 'react-router-dom';

function User() {
  const { id } = useParams();

  return (
    <div>
      <h1>User ID: {id}</h1>
    </div>
  );
}

export default User;



✔ Going to /user/101 will display:

User ID: 101








✔ Supports multiple parameters:

<Route path="order/:orderId/item/:itemId" element={<OrderItem />} />

const { orderId, itemId } = useParams();






⭐ Quick Summary
Feature	Purpose
Nested Routes	Load child components inside parent
Route Params	Pass dynamic values through the URL





*/










const DynamicRouting = () => {
  return (
    <div>DynamicRouting</div>
  )
}

export default DynamicRouting